import pandas as pd
import os

def clean_data(file_path, output_path):

    df = pd.read_csv(file_path)

    df.fillna(df.select_dtypes(include='number').mean(), inplace=True)

    q1 = df['exactPrice'].quantile(0.25)
    q3 = df['exactPrice'].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    df_no_outliers = df[(df['exactPrice'] >= lower_bound) & (df['exactPrice'] <= upper_bound)]

    q1_sqft = df['sqftPrice'].quantile(0.25)
    q3_sqft = df['sqftPrice'].quantile(0.75)
    iqr_sqft = q3_sqft - q1_sqft

    lower_bound_sqft = q1_sqft - 1.5 * iqr_sqft
    upper_bound_sqft = q3_sqft + 1.5 * iqr_sqft

    df_no_outliers_sqft = df[(df['sqftPrice'] >= lower_bound_sqft) & (df['sqftPrice'] <= upper_bound_sqft)]

    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to {output_path}")

if __name__ == '__main__':

    raw_data_path = os.path.join('data', 'house_prices_data.csv')
    cleaned_data_path = os.path.join('data', 'cleaned_house_prices_data.csv')

    clean_data(raw_data_path, cleaned_data_path)