# GastricPredDriver/Validation.py

import os
import pandas as pd
import joblib

def predict(df, model_type='svc'):
    # List of selected genes
    selected_genes = [
        'ARID2', 'ATG2A', 'BAP1', 'BMP2K', 'BTG2', 'CALR', 'CARD11', 'CD58', 'CDH9',
        'CNTN1', 'COL12A1', 'COL14A1', 'CYP2A6', 'FAM174B', 'FBLN2', 'FOXL2', 'GAS7',
        'GRIN2D', 'IRAK1', 'IRS4', 'KLF5', 'KNL1', 'MAP3K1', 'MYC', 'MYOD1', 'OMD',
        'PANK3', 'PCM1', 'PCMTD1', 'PML', 'PRB1', 'PRB3', 'PRRX1', 'RYR1', 'TFAP4',
        'TRRAP', 'TXNIP', 'UBE2A', 'ZNF492'
    ]
    
    # Select features from dataframe
    df_selected = df[selected_genes]
    
    # Construct model path
    model_path = os.path.join(os.path.dirname(__file__), 'models', f'{model_type.lower()}.pkl')
    
    # Check if model file exists
    if not os.path.exists(model_path):
        raise ValueError(f"Model '{model_type}' not found. Ensure the model file exists at {model_path}.")
    
    # Load the model
    model = joblib.load(model_path)
    
    # Make predictions
    y_pred = model.predict(df_selected)
    
    # Add predictions to dataframe
    df['Prediction'] = ['Cancer' if pred == 1 else 'Normal' for pred in y_pred]
    
    # Save predictions to CSV file
    df.to_csv('predictions.csv', index=False)
    
    # Print diagnosis
    count_cancer = y_pred.sum()
    count_normal = len(y_pred) - count_cancer
    percentage_cancer = count_cancer / len(y_pred)
    percentage_normal = count_normal / len(y_pred)
    
    if percentage_cancer > 0.6:
        print(f"Gastric Cancer patient detected, {percentage_cancer*100:.2f}%")
    else:
        print(f"Normal patient detected, {percentage_normal*100:.2f}%")

