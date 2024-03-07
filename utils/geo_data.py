import geopandas as gpd
from shapely.geometry import Point

# Load real estate data into a GeoDataFrame
# Replace 'real_estate.csv' with the actual filename and path to your real estate data
geo_data = gpd.read_file('./src/model_data.csv')

# Load municipality data into a GeoDataFrame
# Replace 'municipality.json' with the actual filename and path to your municipality data
municipality_gdf = gpd.read_file('municipality.json')

# Create Point geometries from latitude and longitude coordinates in real estate data
real_estate_gdf['geometry'] = real_estate_gdf.apply(lambda row: Point(row['longitude'], row['latitude']), axis=1)

# Perform spatial join
joined_data = gpd.sjoin(real_estate_gdf, municipality_gdf, how='left', op='within')

# Drop unnecessary columns from the result
joined_data = joined_data.drop(columns=['index_right'])

# Print the resulting DataFrame with municipality information added
print(joined_data)
