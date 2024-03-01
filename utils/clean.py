import pandas as pd
import numpy as np
from datetime import datetime

def clean_data(raw_data):
    """
    Clean the raw data by performing several tasks:
    1. Remove duplicates in the 'ID' column.
    2. Remove specified columns.
    3. Filter rows where SaleType == 'residential_sale'.
    4. Adjust text format.
    5. Remove leading and trailing spaces from string columns.
    6. Replace the symbol '�' with 'e' in all string columns.
    7. Convert empty values to 0 for specified columns; assumption that if blank then 0.
    8. Convert specified columns to int64 type after filling missing values.
    9. Replace any ConstructionYear > current_year + 10 with NaN.
    10. Write resulting dataframe to a CSV file.

    Parameters:
    raw_data (DataFrame): The raw DataFrame to be cleaned.
    """
    # Task 1: Remove duplicates in the 'ID' column
    raw_data.drop_duplicates(subset='ID', inplace=True)

    # Task 2: Remove specified columns
    columns_to_drop = ['PropertyUrl', 'Street', 'HouseNumber', 'Box', 'Floor']
    raw_data.drop(columns=columns_to_drop, inplace=True)

    # Task 3: Filter rows where SaleType == 'residential_sale'
    raw_data = raw_data[raw_data['SaleType'] == 'residential_sale']

    # Task 4: Adjust text format
    columns_to_str = ['City', 'Region', 'District', 'Province', 'PropertyType', 'PropertySubType', 'SaleType', 'KitchenType', 'Condition', 'EPCScore', 'Property url']
    raw_data[columns_to_str] = raw_data[columns_to_str].applymap(lambda x: x.title() if isinstance(x, str) else x)

    # Task 5: Remove leading and trailing spaces from string columns
    raw_data[columns_to_str] = raw_data[columns_to_str].applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Task 6: Replace the symbol '�' with 'e' in all string columns
    raw_data = raw_data.applymap(lambda x: x.replace('�', 'e') if isinstance(x, str) else x)

    # Task 7: Convert empty values to 0 for specified columns; assumption that if blank then 0
    columns_to_fill_with_zero = ['Furnished', 'Fireplace', 'Terrace', 'TerraceArea', 'Garden', 'GardenArea', 'SwimmingPool']
    raw_data[columns_to_fill_with_zero] = raw_data[columns_to_fill_with_zero].fillna(0)

    # Task 8: Convert specified columns to int64 type after filling missing values
    columns_to_int64 = ['ID', 'PostalCode', 'Price', 'ConstructionYear', 'BedroomCount', 'LivingArea', 'Furnished', 'Fireplace', 'Terrace', 'TerraceArea', 'Garden', 'GardenArea', 'Facades', 'SwimmingPool']
    raw_data[columns_to_int64] = raw_data[columns_to_int64].astype('Int64')

    # Task 9: Replace any ConstructionYear > current_year + 10 with None
    current_year = datetime.now().year
    max_construction_year = current_year + 10
    raw_data['ConstructionYear'] = raw_data['ConstructionYear'].where(raw_data['ConstructionYear'] <= max_construction_year, None)

    # Task 10: Write resulting dataframe to a CSV
    raw_data.to_csv('./src/cleaned/cleaned_data.csv', index=False)

# Load raw data
raw_data = pd.read_csv("./src/raw/raw_data.csv")

# Clean the data
clean_data(raw_data)