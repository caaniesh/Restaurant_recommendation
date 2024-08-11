# Import necessary libraries
import pandas as pd

# Load the datasets
data = pd.read_csv("restaurant_names.csv")

# List all unique cuisines
unique_cuisines = data['Cuisines'].str.split(', ').explode().unique()

# Print the unique cuisines
for cuisine in unique_cuisines:
    print(cuisine)
