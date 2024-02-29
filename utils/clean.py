import pandas as pd

# Importing the data
clean_data = pd.read_csv("https://raw.githubusercontent.com/bear-revels/immo-eliza-scraping-Python_Pricers/main/data/all_property_details.csv")

# create data cleaning function

# Storing locally
clean_data.to_csv('./src/raw/clean_data.csv')
