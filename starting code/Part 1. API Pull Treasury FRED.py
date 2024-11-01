#### Part 1 API Pulling/Data Wrangling/Visualizations
##### 1. Go to https://fred.stlouisfed.org/docs/api/fred/ and register for a free API Key
##### 2. Write a function in Python to pull daily constant maturity yield from 2023-01-01 to 2023-12-31 for the following tenors, which are are 1M, 3M, 6M, 1Y, 2Y, all the way up to 30Y. In FRED database, these are the field names: "DGS1MO", "DGS3MO", "DGS6MO", "DGS1", "DGS2", "DGS3", "DGS5", "DGS7", "DGS10", "DGS20", "DGS30".
##### 3. Store these pulled data into a dataframe and set the date as the index
##### 4. Load the file Bonds_Yields.xlsx. For each bond, calculate its spread over treasury curve. If a bond's WAL falls between 2 points of the Treasury curve, use linear interplation
##### 5. Use visualization to demonstrate the relative value of each sector. Present at least 2 types of visulizations

import requests
import pandas as pd

def fetch_fred_yield(series_id, start_date="2023-01-01", end_date="2023-12-31", api_key="your_api_key"):
    # Define the API URL and parameters here
    
    # Make an API request and handle errors
    
    # Convert response JSON into a DataFrame, setting 'date' as index
    # Convert the 'value' column to numeric and rename it based on series_id
    
    return df[[series_id]]  # Final DataFrame with date index and yield column

# List of Treasury yield series IDs on FRED
tenor_series_ids = [
    "DGS1MO", "DGS3MO", "DGS6MO", "DGS1",  # Short-term yields
    "DGS2", "DGS3", "DGS5",               # Medium-term yields
    "DGS7", "DGS10", "DGS20", "DGS30"     # Long-term yields
]

# Initialize API key

# Fetch data for each tenor, store in a dictionary of DataFrames

# Combine all DataFrames into a single DataFrame, joining on the date index

# Print the number of rows in the final DataFrame
