import pandas as pd
import numpy as np
import random

# Generate state dictionary
state_dict = {f"State_{i}": f"state_{i}" for i in range(1, 28)}

# Generate district names
district_names = [f"District_{i}" for i in range(1, 740)]

# Generate random states for each district
district_state_mapping = {district: random.choice(list(state_dict.keys())) for district in district_names}

# Generate climate data
climate_data = []
for year in range(2018, 2024):
    for district in district_names:
        for quarter in range(4):
            climate_data.append({
                'District': district,
                'Year': year,
                'Temperature': np.random.randint(20, 40),
                'Humidity': np.random.randint(40, 90),
                'Rainfall': np.random.randint(0, 500),
                'Quarter': quarter
            })

# Generate population density data
population_density_data = []
for district in district_names:
    population_density_data.append({
        'District': district,
        'Total_Population': np.random.randint(100000, 10000000),
        'Population_Per_Sq_Km': np.random.randint(50, 5000)
    })

# Generate health records data
health_records_data = []
diseases = ['Chikungunya', 'Dengue', 'Yellow fever', 'Malaria']
for year in range(2018, 2024):
    for district in district_names:
        for quarter in range(4):
            for disease in diseases:
                health_records_data.append({
                    'District': district,
                    'Disease': disease,
                    'Year': year,
                    'No_of_Cases': np.random.randint(0, 100),
                    'Quarter': quarter
                })

# Convert data to DataFrames
climate_df = pd.DataFrame(climate_data)
population_density_df = pd.DataFrame(population_density_data)
health_records_df = pd.DataFrame(health_records_data)

# Save to CSV files
climate_df.to_csv('climate_in_india.csv', index=False)
population_density_df.to_csv('population_density.csv', index=False)
health_records_df.to_csv('health_records.csv', index=False)
