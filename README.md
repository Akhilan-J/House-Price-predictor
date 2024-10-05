House Price Prediction System
This project is a House Price Prediction System built with Python, MySQL, and scikit-learn. It allows users to sign up, sign in, and predict the price of a house based on key features like area, number of rooms, house age, and location. The predictions are stored in a MySQL database along with user information for future reference.

Features:
User Authentication: Users can create an account and securely log in.
Predictive Modeling: A linear regression model trained on housing data to predict house prices based on various factors.
Location-Based Predictions: The model considers the location of the house (urban, suburban, rural) to improve the accuracy of price predictions.
Data Management: User details and predictions are stored in a MySQL database.
Scalable Dataset: The project includes a dataset of 1000 entries with house data, which can easily be expanded.
Tech Stack:
Python: For core programming logic, data handling, and model training.
MySQL: To manage user data and store prediction history.
Pandas: For data manipulation and reading CSV files.
Scikit-learn: Used to train a Linear Regression model for house price prediction.
One-Hot Encoding: Location data (categorical) is one-hot encoded for use in the predictive model.
How it Works:
Sign up: Users register by creating a username and password.
Sign in: Users log in with their credentials.
Predict: The system predicts house prices based on:
Area (in sq. ft.)
Number of rooms
Age of the house (in years)
Location (urban, suburban, rural)
Store Predictions: Predictions are saved in the MySQL database with the user’s details for future reference.
Dataset:
The dataset consists of 1000 entries, with the following features:

Area (sq. ft.)
Number of rooms
House age (years)
Location (urban, suburban, rural)
Price
The dataset is stored in a CSV file, which can be replaced or expanded to include more features or data points as needed.

Installation:
Clone the repository.
Install the required dependencies with pip install -r requirements.txt.
Set up a MySQL database with the necessary tables for user authentication and prediction storage.
Run the script and start using the house price prediction system.
Future Enhancements:
Introduce more features such as proximity to city centers, crime rates, and neighborhood facilities.
Explore more advanced machine learning models for more accurate predictions.
Create a web-based interface for easier access and interaction.

