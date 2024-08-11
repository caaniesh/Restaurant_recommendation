from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load the datasets
data = pd.read_csv("restaurant_names.csv")
data1 = pd.read_csv("restaurant_reviews.csv")

# Data preprocessing
data1 = data1[data1["Rating"] != "Like"]
data1["Rating"] = data1["Rating"].astype("float")
data1.dropna(how='any', inplace=True)
data1["Metadata"] = data1["Metadata"].astype("str")
data1[['No_of_Reviews', 'No_of_Followers']] = data1["Metadata"].str.split(",", expand=True)
data1['No_of_Reviews'] = pd.to_numeric(data1['No_of_Reviews'].astype(str).str.replace(r'\D+', '', regex=True)).fillna(0).astype(int)
data1['No_of_Followers'] = pd.to_numeric(data1['No_of_Followers'].astype(str).str.replace(r'\D+', '', regex=True)).fillna(0).astype(int)
data1["No_of_Followers"] = data1["No_of_Followers"].replace(np.nan, 0)
data1["No_of_Followers"] = data1["No_of_Followers"].astype("int")

# Define the recommendation function
def get_recommendations(cuisine):
    filtered_data = data[data['Cuisines'].str.contains(cuisine, case=False, na=False)]
    top_restaurants = filtered_data[['Name', 'Cuisines', 'Cost', 'Timings', 'Links']].head(20)
    return top_restaurants.to_dict(orient='records')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    cuisine = request.form.get('cuisine')
    recommendations = get_recommendations(cuisine)
    return render_template('recommendations.html', recommendations=recommendations, enumerate=enumerate)


if __name__ == '__main__':
    app.run(debug=True)
