# Code for loading data (CSV, JSON, etc.)
# import zipfile
# import os

# def extract_zip(zip_file_path, extract_to_dir):
#     # Extract the ZIP file
#     with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#         zip_ref.extractall(extract_to_dir)
#     print(f"Dataset extracted to {extract_to_dir}")

# if __name__ == '__main__':
#     # Path to your ZIP file
#     zip_file_path = os.path.join('data', 'house_prices_data.zip')
    
#     # Extract directory
#     extract_to_dir = 'data/'

#     # Extract the ZIP file
#     extract_zip(zip_file_path, extract_to_dir)

import os
import pandas as pd

def load_data(file_path):
    # Load the CSV file into a DataFrame
    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

if __name__ == '__main__':
    # Assuming the dataset is extracted to 'data/house_prices_data.csv'
    data_file_path = os.path.join('data', 'house_prices_data.csv')
    
    # Load the data
    df = load_data(data_file_path)
    
    # Print the first few rows to verify
    if df is not None:
        print(df.head())

