import pandas as pd
import numpy as np

# Assuming 739 districts in India
num_districts = 739

# Generate fake district names
district_names = [f"District_{i}" for i in range(1, num_districts + 1)]

# Generate fake population density data for each district from 2018 to 2023
years = range(2018, 2024)
num_years = len(years)

# Define range for population density (people per square kilometer)
density_range = (100, 20000)

# Generate random population density data for each district and year
population_density_data = {
    'District': [],
    'Year': [],
    'Population_Density': []
}

for district in district_names:
    for year in years:
        population_density_data['District'].append(district)
        population_density_data['Year'].append(year)
        population_density_data['Population_Density'].append(np.random.randint(*density_range))

# Generate disease-wise occurrences data
disease_names = ['Chikungunya', 'Dengue', 'Yellow fever', 'Malaria']
quarters= [0,1,2,3]

# Generate random disease occurrences for each district and year
disease_data = {
    'District': [],
    'Year': [],
    'Disease': [],
    'Occurrences': [],
    "NoOfCases":[],
    "Quarter":[]
}

for district in district_names:
    for year in years:
        for quarte in quarters:
            for disease in disease_names:
                disease_data['District'].append(district)
                disease_data['Year'].append(year)
                disease_data['Disease'].append(disease)
                disease_data['Occurrences'].append(np.random.randint(0, 2))
                disease_data['NoOfCases'].append(np.random.randint(20,20000))
                disease_data['quarter'].append(np.random.randint(0,4))

# Create DataFrames
population_density_df = pd.DataFrame(population_density_data)
disease_occurrences_df = pd.DataFrame(disease_data)

# Save datasets to CSV files
population_density_df.to_csv('population_density_india.csv', index=False)
disease_occurrences_df.to_csv('disease_occurrences_india.csv', index=False)
