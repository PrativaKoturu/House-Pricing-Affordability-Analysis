#Core analysis functions (e.g., calculating average price per region)
# src/analysis.py

import pandas as pd
import os

def calculate_average_price_per_region(file_path):
    df = pd.read_csv(file_path)

    # Assuming there is a 'region' column in the dataset
    avg_exact_price = df.groupby('locality')['exactPrice'].mean()
    avg_sqft_price = df.groupby('locality')['sqftPrice'].mean()

    print("Average exactPrice per region:")
    print(avg_exact_price)
    
    print("\nAverage sqftPrice per region:")
    print(avg_sqft_price)

if __name__ == '__main__':
    segmented_data_path = os.path.join('data', 'segmented_house_prices_data.csv')

    calculate_average_price_per_region(segmented_data_path)
