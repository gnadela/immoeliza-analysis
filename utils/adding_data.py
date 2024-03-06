import pandas as pd

def add_population_density(cleaned_data_file):
    # Importing external dataframes
    conversion_key = pd.read_csv('./src/external_data/Postal_Refnis.csv')
    sector_data = pd.read_csv('./src/external_data/SectorData.csv')

    # Prepping postal_refnis for join
    conversion_key = conversion_key[['Postal code', 'Refnis code', 'Gemeentenaam']]
    conversion_key = conversion_key.rename(columns={'Postal code': 'PostalCode', 'Refnis code': 'CD_REFNIS'})
    # Accounting for overlap in refniscodes
    conversion_aggregated = conversion_key.groupby('CD_REFNIS')['PostalCode'].apply(lambda x: ','.join(x.astype(str))).reset_index()
    # Prepping sector_data for join
    sector_data = sector_data[['CD_REFNIS', 'TOTAL', 'OPPERVLAKKTE IN HM²']]
    # Refniscodes are split in even smaller sections -> merge them to overcome issues (take into account in interpretations)
    aggregated_sector_data = sector_data.groupby('CD_REFNIS', as_index=False).agg({'TOTAL': 'sum', 'OPPERVLAKKTE IN HM²': 'sum'})
    # Merging
    merged_data = pd.merge(aggregated_sector_data, conversion_aggregated, on='CD_REFNIS', how='left')

    # Calculating population density (population per km²)
    merged_data['Area in km²'] = merged_data['OPPERVLAKKTE IN HM²'] * 0.01
    merged_data['PopulationDensity'] = (merged_data['TOTAL'] / merged_data['Area in km²']).round().astype(int)

    # Importing cleaned data into a df
    original = pd.read_csv(cleaned_data_file)
    # Drop all but postalcode & population density
    to_merge = merged_data[['PostalCode', 'PopulationDensity']]

    # Iterating over postalcode string 
    postal_code_density = {}
    for _, row in to_merge.iterrows():
        postal_codes = row['PostalCode'].split(',')
        for code in postal_codes:
            postal_code_density[code] = row['PopulationDensity']

    # Adding a new column for population density in original, based on the mapping
    original['PopulationDensity'] = original['PostalCode'].apply(lambda x: postal_code_density.get(str(x), None))

    # Resaving new data with added column over cleaned_data
    original.to_csv(cleaned_data_file, index=False)
