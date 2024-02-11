import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import random

# Load data
climate_df = pd.read_csv('climate_in_india.csv')
population_density_df = pd.read_csv('population_density.csv')
health_records_df = pd.read_csv('health_records.csv')

# Main title
st.title('Disease Prediction and Analysis')

# Generate district names
district_names = [f"District_{i}" for i in range(1, 740)]

# Generate random states for each district
state_dict = {f"State_{i}": f"state_{i}" for i in range(1, 28)}
district_state_mapping = {district: random.choice(list(state_dict.keys())) for district in district_names}

# Sidebar for filtering options
st.sidebar.header('Filter Data')
selected_quarter = st.sidebar.selectbox('Select Quarter', [0, 1, 2, 3])
selected_state = st.sidebar.selectbox('Select State', list(state_dict.keys()))
selected_district = st.sidebar.selectbox('Select District', district_names)
selected_year = st.sidebar.selectbox('Select Year', range(2018, 2024))

 
st.subheader('Filtered Population Density Data')
filtered_population_density_data = population_density_df[(population_density_df['District'] == selected_district)]
st.write(filtered_population_density_data)

st.subheader('Filtered Health Records Data')
filtered_health_records_data = health_records_df[(health_records_df['Quarter'] == selected_quarter) &
                                                (health_records_df['Year'] == selected_year) &
                                                (health_records_df['District'] == selected_district)]
st.write(filtered_health_records_data)

# Prediction for 2024
st.header('Predicted Disease Cases for 2024')

# Display data in table
st.subheader('Predicted Data for 2024')

# Plotting
st.header('Visualization')

from sklearn.linear_model import LinearRegression

# Visualization function
def visualize_severity(data):
    # Filter data for diseases with severity more than 5
    high_severity_data = data[data['No_of_Cases'] > 5]

    # Group data by district and quarter
    grouped_data = high_severity_data.groupby(['District', 'Quarter']).size().reset_index(name='Count')

    # Pivot the data for better visualization
    pivot_data = grouped_data.pivot(index='District', columns='Quarter', values='Count').fillna(0)

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_title('High Severity Diseases by District and Quarter')
    ax.set_xlabel('Quarter')
    ax.set_ylabel('District')
    im = ax.imshow(pivot_data, cmap='Reds', aspect='auto')
    fig.colorbar(im, ax=ax, label='Number of Cases')
    ax.set_xticks(range(len(pivot_data.columns)))
    ax.set_yticks(range(len(pivot_data.index)))
    
    # Fit linear regression model
    X = grouped_data['Quarter'].values.reshape(-1, 1)
    y = grouped_data['Count'].values
    reg = LinearRegression().fit(X, y)
    
    # Plot linear regression line
    ax.plot(X, reg.predict(X), color='blue', linestyle='dashed', linewidth=2)
    
    plt.tight_layout()
    st.pyplot(fig)

# Call visualization function
visualize_severity(filtered_health_records_data)

