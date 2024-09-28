# Code for loading data (CSV, JSON, etc.)
import pandas as pd
import os

def clean_data(file_path, output_path):
    # Load the dataset
    df = pd.read_csv(file_path)

    # Fill missing values for only numeric columns
    df.fillna(df.select_dtypes(include='number').mean(), inplace=True)

    # Remove outliers (example: for 'exactPrice' column)
    q1 = df['exactPrice'].quantile(0.25)  # Use 'exactPrice' or 'sqftPrice' based on your needs
    q3 = df['exactPrice'].quantile(0.75)
    iqr = q3 - q1

    # Define outlier bounds
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    # Filter out the outliers
    df_no_outliers = df[(df['exactPrice'] >= lower_bound) & (df['exactPrice'] <= upper_bound)]

    # Outlier detection for 'sqftPrice'
    q1_sqft = df['sqftPrice'].quantile(0.25)
    q3_sqft = df['sqftPrice'].quantile(0.75)
    iqr_sqft = q3_sqft - q1_sqft

    # Define outlier bounds for 'sqftPrice'
    lower_bound_sqft = q1_sqft - 1.5 * iqr_sqft
    upper_bound_sqft = q3_sqft + 1.5 * iqr_sqft

    # Filter out the outliers for 'sqftPrice'
    df_no_outliers_sqft = df[(df['sqftPrice'] >= lower_bound_sqft) & (df['sqftPrice'] <= upper_bound_sqft)]

    # Save cleaned data
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == '__main__':
    # Assuming the raw data is in 'data/house_prices_data.csv'
    raw_data_path = os.path.join('data', 'house_prices_data.csv')
    cleaned_data_path = os.path.join('data', 'cleaned_house_prices_data.csv')

    # Clean the data
    clean_data(raw_data_path, cleaned_data_path)