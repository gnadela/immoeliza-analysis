import plotly.express as px
import pandas as pd

# Load data
raw_data = pd.read_csv('../src/raw/raw_data.csv')
data = pd.DataFrame(raw_data)

# Calculate Price per Living Area
data['PricePerLivingArea'] = data['Price'] / data['LivingArea']

# Create a scatter plot using Plotly Express with open-street-map style
fig = px.scatter_mapbox(data, lat='Latitude', lon='Longitude', color='PricePerLivingArea',
                        color_continuous_scale='Plasma', size_max=6, zoom=7,
                        center=dict(lat=data['Latitude'].mean(), lon=data['Longitude'].mean()),
                        hover_name='PricePerLivingArea', title='Price per Living Area',
                        range_color=[data['PricePerLivingArea'].quantile(0.25),
                                     data['PricePerLivingArea'].quantile(0.75)],
                        mapbox_style='open-street-map',
                        hover_data={'City': True, 'Price': True, 'LivingArea': True})

# Update color bar title
fig.update_coloraxes(colorbar_title='Price per Living Area')

# Show the plot
fig.show()
