import pandas as pd

# Importing the data
raw_data = pd.read_csv("https://raw.githubusercontent.com/bear-revels/immo-eliza-scraping-Python_Pricers/main/data/all_property_details.csv")

# 1. Remove duplicates in the 'ID' column
raw_data.drop_duplicates(subset=['ID'], inplace=True)

# 2. Remove the columns 'PropertyURL', 'Street', 'House', 'Box', and 'Floor'
raw_data.drop(columns=['PropertyUrl', 'Street', 'HouseNumber', 'Box', 'Floor'], inplace=True)

# 3. Convert empty values to 0 for specified columns
zero_fill_columns = ['Furnished', 'Fireplace', 'Terrace', 'TerraceArea', 'Garden', 'GardenArea', 'SwimmingPool']
raw_data[zero_fill_columns] = raw_data[zero_fill_columns].fillna(0)

# 4. Convert empty values to None for specified columns
none_fill_columns = ['ConstructionYear', 'BedroomCount', 'LivingArea', 'KitchenType', 'Facades', 'Condition', 'EPCScore']
numeric_columns = raw_data[none_fill_columns].select_dtypes(include='number').columns
object_columns = raw_data[none_fill_columns].select_dtypes(exclude='number').columns

# Fill missing values with None for object columns
raw_data[object_columns] = raw_data[object_columns].fillna(value=None)

# Fill missing values with 0 for numeric columns
raw_data[numeric_columns] = raw_data[numeric_columns].fillna(value=0)

# 5. Convert specified columns to int64 type
int_columns = ['ID', 'PostalCode', 'Price', 'ConstructionYear', 'BedroomCount', 'LivingArea', 'Furnished', 'Fireplace', 'Terrace', 'TerraceArea', 'Garden', 'GardenArea', 'Facades', 'SwimmingPool', 'Latitude', 'Longitude']
raw_data[int_columns] = raw_data[int_columns].astype('int64')

# 6. Convert specified columns to str type
str_columns = ['City', 'Region', 'District', 'Province', 'PropertyType', 'PropertySubType', 'SaleType', 'KitchenType', 'Condition', 'EPCScore', 'Property url']
raw_data[str_columns] = raw_data[str_columns].astype('str')

# 7. Adjust text format
raw_data[str_columns] = raw_data[str_columns].apply(lambda x: x.str.title())

# Storing locally
raw_data.to_csv('./src/clean/cleaned_data.csv')
