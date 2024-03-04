import pandas as pd

# 0
# setup dataframes
# origin: https://statbel.fgov.be/
postal_refnis = pd.read_csv('../src/external_data/Postal_Refnis.csv')
sector_data = pd.read_csv('../src/external_data/SectorData.csv')

# 1
# join postal_refnis[postal code] to sector data, based on refnis code -> [CD_REFNIS]

# A Prepping postal_refnis for join
postal_refnis['CD_REFNIS'] = postal_refnis['Refnis code']
postal_refnis = postal_refnis[['Postal code', 'CD_REFNIS', 'Gemeentenaam']]
pr = postal_refnis.rename(columns={'Postal code': 'PostalCodes'})
# B Prepping sector_data for join
sector_data = sector_data[['CD_REFNIS', 'TOTAL', 'OPPERVLAKKTE IN HM²']]
    # Refniscodes are split in even smaller sections -> merge them to overcome issues (take into account in interpretations)
aggregated_sector_data = sector_data.groupby('CD_REFNIS', as_index=False).agg({'TOTAL': 'sum', 'OPPERVLAKKTE IN HM²': 'sum'})

pr_aggregated = pr.groupby('CD_REFNIS')['PostalCodes'].apply(lambda x: ','.join(x.astype(str))).reset_index()

merged_data = pd.merge(aggregated_sector_data, pr_aggregated, on='CD_REFNIS', how='left')


# 2
# calc population density column

# Calculate population density (population per km²)
merged_data['Area in km²'] = merged_data['OPPERVLAKKTE IN HM²'] * 0.01
merged_data['population density'] = (merged_data['TOTAL'] / merged_data['Area in km²']).round(2)

# Display the first few rows of the DataFrame to verify the new column

print(merged_data.head())

merged_data.to_csv('../src/external_data/PopulationDensity.csv')

# join population density to main cleaned based on postal code -> join on if in postalcodes
    # Import the csv into a new df

    # Drop all but postalcode & density

    # Add to clean data