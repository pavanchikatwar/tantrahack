# Disease Prediction with Climate and Population Data

## Introduction
This project aims to predict the occurrence of diseases such as dengue, malaria, chickenpox, etc., in different districts of India using climate and population density data. The prediction model utilizes historical climate data, population density records, and health records to forecast the probability of disease outbreaks.

## Datasets and Their Parameters
1. **Climate Data**
   - Parameters: Temperature, Humidity, Rainfall, District, Year, Quarter
   
2. **Population Density Data**
   - Parameters: District, Total Population, Population Density (per square kilometer)
   
3. **Health Records Data**
   - Parameters: District, Disease, Year, Number of Cases, Quarter

## Prediction
Using a machine learning model (Random Forest Regression), we predict the possible occurrence of diseases in 2024 based on the selected quarter, state, and district. The prediction model considers climate factors, population density, and historical disease records to estimate the probability of disease outbreaks. Users can interactively select the quarter, state, and district to view the predicted probability of disease cases in 2024.

# Problems
- we didn't got real dataset, so we created fake dataset which is almost symetrical so the visualiztion is not proper , should need to work on 
