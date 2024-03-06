# immoeliza-analysis

[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## 🛠️ Updates
N/A

## 📒 Description

This repository contains a Python project aimed at loading, organizing, normalizing, and cleaning real estate data scraped from an earlier project. The cleaned data is then analyzed and cataloged in notebooks within the `analysis` folder. Subsequently, the data is further refined for future modeling efforts. The project also includes a presentation for client updates located in the `reports` folder.

## 📦 Repo structure

```
.
├── analysis/
│ ├── *Final_Notebook.ipynb
│ ├── Bears_Notebook.ipynb
│ ├── Caros_Notebook.ipynb
│ ├── Geraldines_Notebook.ipynb
│ └── Viktors_Notebook.ipynb
├── reports/
│ └── presentation.pdf
├── src/
│ ├── external_data/
│ │ ├── PopulationDensity.csv
│ │ ├── Postal_Refnis.csv
│ │ ├── SectorData.csv
│ │ └── checkforlargeareaaggregations.csv
│ ├── raw_data.csv
│ ├── clean_data.csv
│ ├── model_data.csv
│ ├── adding_data.py
│ ├── clean.py
│ ├── data_import.py
│ └── model_ready.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## 🎮 Usage

1. **Clone the repository**: 

    ```
    git clone <repository_url>
    ```

2. **Install dependencies**: 

    ```
    pip install -r requirements.txt
    ```

3. **Run the program**: 

    ```
    python main.py
    ```

    This will load data from a previous project that scraped real estate data, clean the data, add population density information, and generate three CSV files (`raw_data.csv`, `clean_data.csv`, and `model_data.csv`) in the `src` folder.

## ⏱️ Timeline

The development of this project took 5 days for completion.

## 📋 Libraries and Functions

### `data_import.py`

- `import_data()`: Imports raw data from a CSV file using `pandas`, storing it locally and returning a DataFrame.

### `clean.py`

- `clean_data(raw_data)`: Cleans the raw data by performing several tasks:
  1. Drops rows with empty values in 'Price' and 'LivingArea' columns.
  2. Removes duplicates in the 'ID' column and where all columns but 'ID' are equal.
  3. Converts empty values to 0 for specified columns: 'Furnished', 'Fireplace', 'Terrace', 'TerraceArea', 'Garden', 'GardenArea', 'SwimmingPool', 'BidStylePricing', 'ViewCount', 'bookmarkCount'.
  4. Filters rows where SaleType == 'residential_sale' and BidStylePricing == 0.
  5. Removes specified columns: 'PropertyUrl', 'Street', 'HouseNumber', 'Box', 'Floor', 'SaleType', 'BidStylePricing', 'Property url'.
  6. Adjusts text format for specified columns: 'City', 'Region', 'District', 'Province', 'PropertyType', 'PropertySubType', 'KitchenType', 'Condition', 'EPCScore'.
  7. Removes leading and trailing spaces from string columns.
  8. Replaces the symbol '�' with 'e' in all string columns.
  9. Fills missing values with None and converts specified columns to float64 type: 'EnergyConsumptionPerSqm'.
  10. Converts specified columns to Int64 type: 'ID', 'PostalCode', 'ConstructionYear', 'BedroomCount', 'Furnished', 'Fireplace', 'Terrace', 'Garden', 'Facades', 'SwimmingPool', 'bookmarkCount', 'ViewCount'.
  11. Replaces any ConstructionYear > current_year + 10 with None.
  12. Trims text after and including '_' from the 'EPCScore' column.
  13. Converts 'ListingCreateDate', 'ListingExpirationDate', and 'ListingCloseDate' to Date type with standard DD/MM/YYYY format.
  14. Replaces values less than or equal to 0 in 'EnergyConsumptionPerSqm' with 0.
  15. Calculates 'TotalArea'.
  16. Calculates 'PricePerLivingSquareMeter'.
  17. Calculates 'PricePerTotalSquareMeter'.
  18. Converts string values to numeric values using dictionaries for specified columns: 'Condition', 'KitchenType'.
  19. Writes resulting dataframe to a CSV.

### `adding_data.py`

- `add_population_density(cleaned_data_file)`: Adds population density information to the cleaned data by importing external dataframes, aggregating and merging data, calculating population density, and merging the results back into the original data.

### `model_ready.py`

- `remove_outliers(data, column)`: Removes outliers from the data based on the specified column using the Interquartile Range (IQR) method.
- `prepare_model_data(cleaned_data_file)`: Prepares the cleaned data for modeling by removing outliers from specified columns and saving the resulting DataFrame to a CSV file.

## 📌 Personal Situation

This project was completed as part of the AI Boocamp at BeCode.org by team Python Pricers. 

Connect with the Python Pricers on LinkedIn:
1. [Bear Revels](https://www.linkedin.com/in/bear-revels/)
2. [Caroline Van Hoeke](https://www.linkedin.com/in/caroline-van-hoeke-8a3b87123/)
3. [Geraldine Nadela](https://www.linkedin.com/in/geraldine-nadela-60827a11)
4. [Viktor Cosaert](https://www.linkedin.com/in/viktor-cosaert/)
