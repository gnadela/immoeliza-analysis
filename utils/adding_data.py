import pandas as pd

# setup dataframes
# origin: https://statbel.fgov.be/
postal_refnis = pd.read_csv('../src/external_data/Postal_Refnis.csv')
sector_data = pd.read_csv('../src/external_data/SectorData.csv')

# A Prepping postal_refnis for join
postal_refnis = postal_refnis[['Postal code', 'Refnis code', 'Gemeentenaam']]
pr = postal_refnis.rename(columns={'Postal code': 'PostalCode', 'Refnis code': 'CD_REFNIS'})
pr_aggregated = pr.groupby('CD_REFNIS')['PostalCode'].apply(lambda x: ','.join(x.astype(str))).reset_index()
# B Prepping sector_data for join
sector_data = sector_data[['CD_REFNIS', 'TOTAL', 'OPPERVLAKKTE IN HM²']]
    # Refniscodes are split in even smaller sections -> merge them to overcome issues (take into account in interpretations)
aggregated_sector_data = sector_data.groupby('CD_REFNIS', as_index=False).agg({'TOTAL': 'sum', 'OPPERVLAKKTE IN HM²': 'sum'})

merged_data = pd.merge(aggregated_sector_data, pr_aggregated, on='CD_REFNIS', how='left')

# calc population density column
# Calculate population density (population per km²)
merged_data['Area in km²'] = merged_data['OPPERVLAKKTE IN HM²'] * 0.01
merged_data['population density'] = (merged_data['TOTAL'] / merged_data['Area in km²']).round(2)

# Display the first few rows of the DataFrame to verify the new column

print(merged_data.head())
large_area_combinations = merged_data[merged_data['PostalCode'].str.len() > 15]

merged_data.to_csv('../src/external_data/PopulationDensity.csv')
large_area_combinations.to_csv('../src/external_data/checkforlargeareaaggregations.csv')

# join population density to main cleaned based on postal code -> join on if in postalcodes
    # Import the csv into a new df

    # Drop all but postalcode & density

    # Add to clean data