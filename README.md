# Project: Restaurant Recommendation System                                                       

The Restaurant Recommendation System is a Flask-based web application designed to help users find the best restaurants based on their cuisine preferences. This project utilizes datasets of restaurant names and reviews to provide recommendations and allows users to submit feedback on their experience.

## Features
Cuisine Selection: Users can choose from various cuisine types to get restaurant recommendations.
Restaurant Recommendations: Displays a list of top restaurants based on the selected cuisine.
Feedback Form: Users can submit feedback about their experience or the application itself.
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
index.html: The homepage with a form for selecting cuisine and providing feedback.
recommendations.html: The page displaying the list of recommended restaurants.
