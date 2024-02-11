import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score

# Load data
@st.cache_data
def load_data():
    # Load datasets
    population_density_data = pd.read_csv('population_density_india.csv')
    climate_data = pd.read_csv('climate_data_india.csv')
    disease_occurrences_data = pd.read_csv('disease_occurrences_india.csv')

    # Merge data
    data = pd.merge(population_density_data, climate_data, on=['District', 'Year'])
    data = pd.merge(data, disease_occurrences_data, on=['District', 'Year'])
    return data

# Train model
def train_model(data):
    X = data.drop(columns=['District', 'Year', 'Disease', 'Occurrences'])
    y = data['Occurrences']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = XGBClassifier()
    model.fit(X_train, y_train)
    return model, X_test, y_test

# Main function
def main():
    st.title('Disease Occurrence Prediction')

    data = load_data()

    # Train model
    model, X_test, y_test = train_model(data)


    # Display model performance
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    st.write(f'Model Accuracy: {accuracy}')

    # User input
    st.sidebar.header('User Input')
    district = st.sidebar.selectbox('Select District', data['District'].unique())
    year = st.sidebar.number_input('Year', min_value=2018, max_value=2023)
    # Add other input fields as needed

    # Make prediction
    input_data = data[(data['District'] == district) & (data['Year'] == year)]
    prediction = model.predict(input_data.drop(columns=['District', 'Year', 'Disease', 'Occurrences']))
    
    st.subheader('Prediction')
    st.write('Disease Occurrence:', prediction)

if __name__ == '__main__':
    main()
