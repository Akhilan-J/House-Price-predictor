import mysql.connector as s
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import warnings
from sklearn.exceptions import DataConversionWarning

# Ignore warnings
warnings.filterwarnings(action='ignore', category=UserWarning)

# MySQL connection setup
def connect_db():
    try:
        connection = s.connect(host="localhost", user="root", passwd="rootroot", database="project")
        if connection.is_connected():
            print("Connected to database")
            return connection
    except Exception as e:
        print(f"Connection error: {e}")
        return None

# Signup function
def signup(cursor):
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute("SELECT username FROM signup")
    users = cursor.fetchall()

    if any(user[0] == username for user in users):
        print("Username already exists. Please choose another.")
        return False

    cursor.execute("INSERT INTO signup (username, password) VALUES (%s, %s)", (username, password))
    mycon.commit()
    return True

# Signin function
def signin(cursor):
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute("SELECT * FROM signup WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    if user:
        return user[0]
    print("Invalid credentials. Try again.")
    return None

# Load data from CSV and train the model
def load_and_train_model(csv_file):
    df = pd.read_csv(csv_file)
    
    # One-Hot Encoding for the location column
    column_transformer = ColumnTransformer([('encoder', OneHotEncoder(), ['location'])], remainder='passthrough')
    X = df[['location', 'area', 'no_of_rooms', 'age']]
    X_encoded = column_transformer.fit_transform(X)
    
    y = df['price']

    model = LinearRegression()
    model.fit(X_encoded, y)
    
    return model, column_transformer

# Predict house price
def predict_price(model, column_transformer):
    area = int(input("Enter area: "))
    rooms = int(input("Enter number of rooms: "))
    age = int(input("Enter the age of the house: "))
    location = input("Enter location (urban/suburban/rural): ")

    # Transform user input using the column transformer
    user_input = pd.DataFrame([[location, area, rooms, age]], columns=['location', 'area', 'no_of_rooms', 'age'])
    user_input_encoded = column_transformer.transform(user_input)

    predicted_price = model.predict(user_input_encoded)[0]
    print(f"The predicted price of the house is: {int(predicted_price)}")
    return predicted_price

# Record prediction into database
def save_prediction(cursor, username, predicted_price):
    cursor.execute("INSERT INTO data (username, predicted_price) VALUES (%s, %s)", (username, predicted_price))
    mycon.commit()

# Main execution flow
mycon = connect_db()
if mycon:
    cursor = mycon.cursor()

    if signup(cursor):
        user = None
        while not user:
            user = signin(cursor)

        print("Signin successful")
        model, column_transformer = load_and_train_model("E:/csv/house_data_with_location.csv")
        predicted_price = predict_price(model, column_transformer)
        save_prediction(cursor, user, predicted_price)
