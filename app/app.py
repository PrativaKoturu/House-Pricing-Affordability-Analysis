import streamlit as st
import pandas as pd
import os
import plotly.express as px

def main():
    st.title("Housing Affordability Analysis")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, '..', 'data', 'segmented_house_prices_data.csv')
    df = pd.read_csv(data_path)

    st.sidebar.header("Filters")
    
    price_range = st.sidebar.slider('Select Price Range', 
                                    min_value=int(df['exactPrice'].min()), 
                                    max_value=int(df['exactPrice'].max()), 
                                    value=(10000, 50000))
    filtered_df = df[(df['exactPrice'] >= price_range[0]) & (df['exactPrice'] <= price_range[1])]
    
    property_types = st.sidebar.multiselect('Select Property Types:', 
                                            df['propertyType'].unique())
    if property_types:
        filtered_df = filtered_df[filtered_df['propertyType'].isin(property_types)]

    locality = st.sidebar.multiselect('Select Localities:', 
                                    df['locality'].unique())
    if locality:
        filtered_df = filtered_df[filtered_df['locality'].isin(locality)]

    bedrooms = st.sidebar.slider('Select Number of Bedrooms', 
                                min_value=int(df['bedrooms'].min()), 
                                max_value=int(df['bedrooms'].max()), 
                                value=(1, int(df['bedrooms'].max())))
    filtered_df = filtered_df[filtered_df['bedrooms'].between(bedrooms[0], bedrooms[1])]

    bathrooms = st.sidebar.slider('Select Number of Bathrooms', 
                                min_value=int(df['bathrooms'].min()), 
                                max_value=int(df['bathrooms'].max()), 
                                value=(1, int(df['bathrooms'].max())))
    filtered_df = filtered_df[filtered_df['bathrooms'].between(bathrooms[0], bathrooms[1])]

    st.subheader("Summary Statistics")
    st.write(f"Total Listings: {filtered_df.shape[0]}")
    st.write(f"Average Price: ${filtered_df['exactPrice'].mean():,.2f}")

    st.subheader("Price Distribution by Locality")
    fig = px.bar(filtered_df, x='locality', y='exactPrice', color='price_segment', title="Price Distribution by Locality")
    st.plotly_chart(fig)

    st.subheader("Property Types Distribution")
    property_type_counts = filtered_df['propertyType'].value_counts()
    fig2 = px.pie(values=property_type_counts.values, names=property_type_counts.index, title='Property Types Distribution')
    st.plotly_chart(fig2)

    st.subheader("Price vs. Bedrooms")
    fig3 = px.scatter(filtered_df, x='bedrooms', y='exactPrice', color='price_segment', title="Price vs. Bedrooms")
    st.plotly_chart(fig3)

    st.sidebar.header("Instructions")
    st.sidebar.write("""
        Use the filters on the left to refine your search for properties.
        Adjust the price range, select property types, localities, and the number of bedrooms and bathrooms to see updated results.
        Explore the visualizations for better insights into the housing market.
    """)

if __name__ == '__main__':
    main()
