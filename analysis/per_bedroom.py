import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Get raw data
raw_data = pd.read_csv('https://raw.githubusercontent.com/gnadela/immoeliza-analysis/main/src/cleaned_data.csv')

# Filter the dataset for properties
filtered_data = raw_data[(raw_data['BedroomCount'] >= 0) & 
                         (raw_data['BedroomCount'] <= 12) & 
                         (raw_data['Price'] > 0) & 
                         (raw_data['Price'] <= 1000000) &
                         (raw_data['LivingArea'] > 0)]  # Make sure LivingArea is greater than 0

# Calculate PricePerLivingArea
filtered_data['PricePerLivingArea'] = filtered_data['Price'] / filtered_data['LivingArea']

# Set up the figure and axis
plt.figure(figsize=(12, 6))

# Create kernel density estimate plots for the prices per living area of properties with different bedroom counts
for bedroom_count in range(0, 13):
    sns.kdeplot(data=filtered_data[filtered_data['BedroomCount'] == bedroom_count]['PricePerLivingArea'], 
                label=f'{bedroom_count} Bedrooms')

# Set x-axis limit
plt.xlim(0, 10000)

# Add labels and title
plt.xlabel('Price per Living Area')
plt.ylabel('Density')
plt.title('Density of Prices per Living Area for Properties with Different Bedroom Counts')

# Show the legend
plt.legend(title='Bedroom Count')

# Show the plot
plt.show()


 