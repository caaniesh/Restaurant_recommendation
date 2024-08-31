# Project: Restaurant Recommendation System                                                       

The Restaurant Recommendation System is a user-friendly web application designed to help users find the best restaurants based on their cuisine preferences. This project utilizes datasets of hyderabad restaurant names and reviews to provide recommendations.

## Features
Cuisine Selection: Users can choose from various cuisine types to get restaurant recommendations.
Restaurant Recommendations: Displays a list of top restaurants based on the selected cuisine.
Data Processing: Includes preprocessing of restaurant review data for better recommendations.
## Technologies Used
Flask: A lightweight WSGI web application framework for Python.
Pandas: Data manipulation and analysis library for Python.
NumPy: Library for numerical operations in Python.
## Project Structure
app.py: The main Flask application file that defines routes and handles requests.
restaurant_names.csv: CSV file containing restaurant names and details.
restaurant_reviews.csv: CSV file containing restaurant reviews and ratings.
templates/
index.html: The homepage with a form for selecting cuisine.
recommendations.html: The page displaying the list of recommended restaurants.
## Setup and Installation
To set up and run the Restaurant Recommendation project locally, follow these steps:

### 1. Clone the Repository:
git clone https://github.com/caaniesh/Restaurant_recommendation.git
### 2.  Navigate to the Project Directory:
cd Restaurant_recommendation
### 3. Folder Structure
your_project/
 app.py;
 restaurant_names.csv;
 restaurant_reviews.csv;
 templates/
 (index.html
 recommendations.html)
 ### 4. Run the Flask Application:
 python app.py
 
The application will be available at http://127.0.0.1:5000/ by default.


    
    

