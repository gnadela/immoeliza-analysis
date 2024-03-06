import pandas as pd
import plotly.express as px

# et raw data
raw_data = pd.read_csv("https://raw.githubusercontent.com/bear-revels/immo-eliza-scraping-Python_Pricers/main/data/all_property_details.csv")
# raw_data = pd.read_csv('https://raw.githubusercontent.com/gnadela/immoeliza-analysis/main/src/cleaned_data.csv')

# Filter data for PropertyType
data = raw_data[raw_data['PropertyType'] == 'HOUSE']

# Group data by postal code and calculate median latitude, longitude, and prices
median_data = data.groupby('PostalCode').agg({'Latitude': 'median', 'Longitude': 'median', 'Price': 'median'}).reset_index()

# Get the first instance of 'City' for each postal code
first_city = data.groupby('PostalCode')['City'].first().reset_index()

# Count the number of properties per postal code
count_data = data.groupby('PostalCode').size().reset_index(name='PropertyCount')

# Merge median data with count data
merged_data = pd.merge(median_data, count_data, on='PostalCode')

# Merge with first instance of city data
merged_data = pd.merge(merged_data, first_city, on='PostalCode')

# Create a scatter plot using Plotly Express with open-street-map style
fig = px.scatter_mapbox(merged_data, lat='Latitude', lon='Longitude', color='Price',
                        color_continuous_scale='Plasma', 
                        size='PropertyCount',  # Marker size depends on the 'PropertyCount' column
                        zoom=7,
                        center=dict(lat=merged_data['Latitude'].mean(), lon=merged_data['Longitude'].mean()),
                        hover_name='PostalCode', title='Median HOUSE Price per Postal Code',
                        range_color=[merged_data['Price'].quantile(0.1), merged_data['Price'].quantile(0.9)],
                        mapbox_style='open-street-map',
                        custom_data=['PostalCode', 'City', 'Price', 'PropertyCount'])

# Update hover information 
fig.update_traces(hovertemplate='<b>Postal Code:</b> %{customdata[0]}<br>'
                                  '<b>City:</b> %{customdata[1]}<br>'
                                  '<b>Median Price:</b> %{customdata[2]}<br>'
                                  '<b>Number of Properties:</b> %{customdata[3]}')

# Update color bar title
fig.update_coloraxes(colorbar_title='HOUSE Price')

# Show the plot
fig.show()

