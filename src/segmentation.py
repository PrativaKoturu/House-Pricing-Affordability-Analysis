# Code for segmenting properties into price brackets
# src/segmentation.py

import pandas as pd
import os

def segment_data(file_path, output_path):
    df = pd.read_csv(file_path)

    # Define price segments based on 'exactPrice'
    bins = [0, 10000, 30000, float('inf')]  
    labels = ['low', 'mid', 'high']
    df['price_segment'] = pd.cut(df['exactPrice'], bins=bins, labels=labels)

    # Save segmented data
    df.to_csv(output_path, index=False)
    print(f"Segmented data saved to {output_path}")

if __name__ == '__main__':
    cleaned_data_path = os.path.join('data', 'cleaned_house_prices_data.csv')
    segmented_data_path = os.path.join('data', 'segmented_house_prices_data.csv')

    segment_data(cleaned_data_path, segmented_data_path)
