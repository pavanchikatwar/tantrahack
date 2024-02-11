import pandas as pd
import numpy as np

# Assuming 739 districts in India
num_districts = 739

# Generate fake district names
district_names = [f"District_{i}" for i in range(1, num_districts + 1)]

# Generate fake climate data for each district from 2018 to 2023
years = range(2018, 2024)
num_years = len(years)

# Define ranges for climate data
temperature_range = (20, 40)  # Temperature in Celsius
humidity_range = (40, 90)     # Humidity in percentage
rainfall_range = (0, 500)     # Rainfall in mm

# Generate random climate data for each district and year
climate_data = {
    'District': [],
    'Year': [],
    'Temperature': [],
    'Humidity': [],
    'Rainfall': []
}

for district in district_names:
    for year in years:
        climate_data['District'].append(district)
        climate_data['Year'].append(year)
        climate_data['Temperature'].append(np.random.randint(*temperature_range))
        climate_data['Humidity'].append(np.random.randint(*humidity_range))
        climate_data['Rainfall'].append(np.random.randint(*rainfall_range))

# Create DataFrame
climate_df = pd.DataFrame(climate_data)

# Save dataset to CSV file
climate_df.to_csv('climate_data_india.csv', index=False)
