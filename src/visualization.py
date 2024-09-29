import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_price_segments(file_path):
    df = pd.read_csv(file_path)

    sns.countplot(x='price_segment', data=df)
    plt.title('Distribution of Price Segments based on exactPrice')
    plt.xlabel('Price Segment')
    plt.ylabel('Count')
    plt.show()

def plot_avg_price_per_region(file_path):
    df = pd.read_csv(file_path)

    region_avg_price = df.groupby('region').agg({'exactPrice': 'mean', 'sqftPrice': 'mean'}).reset_index()

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    sns.barplot(x='region', y='exactPrice', data=region_avg_price, ax=ax[0])
    ax[0].set_title('Average exactPrice per Region')
    ax[0].set_ylabel('exactPrice')

    sns.barplot(x='region', y='sqftPrice', data=region_avg_price, ax=ax[1])
    ax[1].set_title('Average sqftPrice per Region')
    ax[1].set_ylabel('sqftPrice')

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    segmented_data_path = os.path.join('data', 'segmented_house_prices_data.csv')

    plot_price_segments(segmented_data_path)
    plot_avg_price_per_region(segmented_data_path)
