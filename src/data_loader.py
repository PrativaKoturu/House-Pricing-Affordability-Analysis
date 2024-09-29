# Code for loading data (CSV, JSON, etc.)
# import zipfile
# import os

# def extract_zip(zip_file_path, extract_to_dir):
#
#     with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#         zip_ref.extractall(extract_to_dir)
#     print(f"Dataset extracted to {extract_to_dir}")

# if __name__ == '__main__':
#
#     zip_file_path = os.path.join('data', 'house_prices_data.zip')
    
#
#     extract_to_dir = 'data/'

#
#     extract_zip(zip_file_path, extract_to_dir)

import os
import pandas as pd

def load_data(file_path):

    try:
        df = pd.read_csv(file_path)
        print(f"Data loaded successfully from {file_path}")
        return df
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

if __name__ == '__main__':
    
    data_file_path = os.path.join('data', 'house_prices_data.csv')
    
    df = load_data(data_file_path)
    
    if df is not None:
        print(df.head())

