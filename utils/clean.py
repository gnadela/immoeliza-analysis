import pandas as pd
from datetime import datetime

def clean_data(raw_data):
    """
    Clean the raw data by performing several tasks:
    1. Remove duplicates
    2. Remove unused columns
    3. Filter to SaleType == 'residential_sale' and BidStylePricing == 0
    4. Adjust text format
    5. Remove leading and trailing spaces from string columns
    6. Replace the symbol '�' with 'e' in all string columns
    7. Convert empty values to 0 for specified columns; assumption that if blank then 0
    8. Convert specified columns to float64 type after filling missing values
    9. Convert specified columns to Int64 type
    10. Replace any ConstructionYear > current_year + 10 with None
    11. Trim text after and including '_' from the 'EPCScore' column
    12. Remove SaleType column
    13. Convert 'ListingCreateDate', 'ListingExpirationDate', and 'ListingCloseDate' to Date type with standard DD/MM/YYYY format
    14. Drop rows with empty values in 'Price', 'LivingArea', or 'EnergyConsumptionPerSqm'
    15. Calculate 'TotalArea'
    16. Calculate 'PricePerLivingSquareMeter'
    17. Calculate 'PricePerTotalSquareMeter'
    18. Calculate 'PricePerKWConsumption'
    19. Write resulting dataframe to a CSV

    Parameters:
    raw_data (DataFrame): The raw DataFrame to be cleaned
    """
    # Task 1: Remove duplicates in the 'ID' column and where all columns but 'ID' are equal
    raw_data.drop_duplicates(subset='ID', inplace=True)
    raw_data.drop_duplicates(subset=raw_data.columns.difference(['ID']), keep='first', inplace=True)

    # Task 2: Remove specified columns
    columns_to_drop = ['PropertyUrl', 'Street', 'HouseNumber', 'Box', 'Floor']
    raw_data.drop(columns=columns_to_drop, inplace=True)

    # Task 3: Filter rows where SaleType == 'residential_sale' and BidStylePricing == 0
    raw_data = raw_data[(raw_data['SaleType'] == 'residential_sale') & (raw_data['BidStylePricing'] == 0)].copy()

    # Task 4: Adjust text format
    columns_to_str = ['City', 'Region', 'District', 'Province', 'PropertyType', 'PropertySubType', 'KitchenType', 'Condition', 'EPCScore']

    def adjust_text_format(x):
        if isinstance(x, str):
            return x.title()
        else:
            return x

    raw_data.loc[:, columns_to_str] = raw_data.loc[:, columns_to_str].applymap(adjust_text_format)

    # Task 5: Remove leading and trailing spaces from string columns
    raw_data.loc[:, columns_to_str] = raw_data.loc[:, columns_to_str].apply(lambda x: x.str.strip() if isinstance(x, str) else x)

    # Task 6: Replace the symbol '�' with 'e' in all string columns
    raw_data = raw_data.applymap(lambda x: x.replace('�', 'e') if isinstance(x, str) else x)

    # Task 7: Convert empty values to 0 for specified columns; assumption that if blank then 0
    columns_to_fill_with_zero = ['Furnished', 'Fireplace', 'Terrace', 'TerraceArea', 'Garden', 'GardenArea', 'SwimmingPool', 'BidStylePricing']
    raw_data[columns_to_fill_with_zero] = raw_data[columns_to_fill_with_zero].fillna(0)

    # Task 8: Convert specified columns to float64 type after filling missing values
    columns_to_float64 = ['BidStylePricing', 'EnergyConsumptionPerSqm', 'bookmarkCount', 'ViewCount']
    raw_data[columns_to_float64] = raw_data[columns_to_float64].astype(float)

    # Task 9: Convert specified columns to Int64 type
    columns_to_int64 = ['ID', 'PostalCode', 'Price', 'ConstructionYear', 'BedroomCount', 'LivingArea', 'Furnished', 'Fireplace', 'Terrace', 'TerraceArea', 'Garden', 'GardenArea', 'Facades', 'SwimmingPool', 'bookmarkCount', 'ViewCount']
    raw_data[columns_to_int64] = raw_data[columns_to_int64].astype('Int64')

    # Task 10: Replace any ConstructionYear > current_year + 10 with None
    current_year = datetime.now().year
    max_construction_year = current_year + 10
    raw_data['ConstructionYear'] = raw_data['ConstructionYear'].where(raw_data['ConstructionYear'] <= max_construction_year, None)

    # Task 11: Trim text after and including '_' from the 'EPCScore' column
    raw_data['EPCScore'] = raw_data['EPCScore'].str.split('_').str[0]

    # Task 12: Remove SaleType column
    raw_data.drop(columns=['SaleType'], inplace=True)

    # Task 13: Convert 'ListingCreateDate', 'ListingExpirationDate', and 'ListingCloseDate' to Date type with "%Y-%m-%d" format
    date_columns = ['ListingCreateDate', 'ListingExpirationDate', 'ListingCloseDate']
    for col in date_columns:
        raw_data[col] = pd.to_datetime(raw_data[col]).dt.date

    # Task 14: Drop rows with empty values in 'Price', 'LivingArea', or 'EnergyConsumptionPerSqm'
    raw_data.dropna(subset=['Price', 'LivingArea', 'EnergyConsumptionPerSqm'], how='any', inplace=True)

    # Task 15: Calculate 'TotalArea'
    raw_data['TotalArea'] = raw_data['LivingArea'] + raw_data['GardenArea'] + raw_data['TerraceArea']

    # Task 16: Calculate 'PricePerLivingSquareMeter'
    raw_data['PricePerLivingSquareMeter'] = (raw_data['Price'] / raw_data['LivingArea']).round().astype(int)

    # Task 17: Calculate 'PricePerTotalSquareMeter'
    raw_data['PricePerTotalSquareMeter'] = (raw_data['Price'] / raw_data['TotalArea']).round().astype(int)

    # Task 18: Calculate 'PricePerKWConsumption'
    raw_data['PricePerKWConsumption'] = (raw_data['Price'] / raw_data['EnergyConsumptionPerSqm']).round().astype(int)

    # Task 19: Write resulting dataframe to a CSV
    raw_data.to_csv('./src/cleaned_data.csv', index=False)

if __name__ == "__main__":
    # Load raw data
    raw_data = pd.read_csv("./src/raw_data.csv")

    # Clean the data
    clean_data(raw_data)
