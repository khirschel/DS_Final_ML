#here is code to load a csv

import pandas as pd

# Function to load and display a CSV
def load_data(csv_path):
    try:
        # Load the CSV file
        data = pd.read_csv(csv_path)
        print("CSV loaded successfully!")
        print("Here are the first few rows:")
        #print(data.head())  # Display the first 5 rows
        return data
    except FileNotFoundError:
        print(f"Error: The file '{csv_path}' was not found.")
        
    
