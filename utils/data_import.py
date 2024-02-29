import pandas as pd

# Importing the data
raw_data = pd.read_csv("https://raw.githubusercontent.com/bear-revels/immo-eliza-scraping-Python_Pricers/main/data/all_property_details.csv")

# Storing locally
raw_data.to_csv('./src/raw/raw_data.csv')