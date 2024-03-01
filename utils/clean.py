import pandas as pd

def clean_data(raw_data):
    """
    Clean the raw data by performing several tasks:
    1. Remove duplicates in the 'ID' column.
    2. Remove specified columns.
    3. Convert empty values to 0 for specified columns.
    4. Convert specified columns to int64 type after filling missing values.
    5. Convert specified columns to str type.
    6. Adjust text format.
    7. Write resulting dataframe to a CSV file.

    Parameters:
    raw_data (DataFrame): The raw DataFrame to be cleaned.
    """
    # Task 1: Remove duplicates in the 'ID' column
    raw_data.drop_duplicates(subset='ID', inplace=True)

    # Task 2: Remove specified columns
    columns_to_drop = ['PropertyUrl', 'Street', 'HouseNumber', 'Box', 'Floor']
    raw_data.drop(columns=columns_to_drop, inplace=True)

    # Task 3: Convert empty values to 0 for specified columns
    columns_to_fill_with_zero = ['Furnished', 'Fireplace', 'Terrace', 'TerraceArea', 'Garden', 'GardenArea', 'SwimmingPool']
    raw_data[columns_to_fill_with_zero] = raw_data[columns_to_fill_with_zero].fillna(0)

    # Task 4: Convert specified columns to int64 type after filling missing values
    columns_to_int64 = ['ID', 'PostalCode', 'Price', 'ConstructionYear', 'BedroomCount', 'LivingArea', 'Furnished', 'Terrace', 'TerraceArea', 'Garden', 'GardenArea', 'Facades', 'SwimmingPool', 'Latitude', 'Longitude']
    raw_data[columns_to_int64] = raw_data[columns_to_int64].fillna(-1).astype('int64')

    # Task 5: Convert specified columns to str type
    columns_to_str = ['City', 'Region', 'District', 'Province', 'PropertyType', 'PropertySubType', 'SaleType', 'KitchenType', 'Condition', 'EPCScore', 'Property url']
    raw_data[columns_to_str] = raw_data[columns_to_str].astype('str')

    # Task 6: Adjust text format
    raw_data[columns_to_str] = raw_data[columns_to_str].applymap(lambda x: x.title() if isinstance(x, str) else x)

    # Task 7: Write resulting dataframe to a CSV
    raw_data.to_csv('./src/cleaned/cleaned_data.csv', index=False)

# Load raw data
raw_data = pd.read_csv("./src/raw/raw_data.csv")

# Clean the data
clean_data(raw_data)