import pandas as pd
import numpy as np

feature_table = {}

def load_csv(filepath):
    dataset = pd.read_csv(filepath)
    return dataset

def check_shape(df):
    shape = df.shape
    return shape

def reshape_data(df):
    shape = check_shape(df)
    num_rows, num_columns = shape

    if num_rows > 5000:
        df_reshape = df.iloc[:5000, :].copy()  # Create a copy to avoid SettingWithCopyWarning
    else:
        df_reshape = df.copy()

    return df_reshape

def find_null(df):
    null = df.isnull().sum()
    return null

def var_type(df): # not used
    feature_table = {}
    for col in df.columns:
        if df[col].dtype == 'object':
            # Check if the column contains categorical data
            if pd.api.types.is_categorical_dtype(df[col]):
                feature_table[col] = 'categorical'
            else:
                feature_table[col] = 'text' 
        elif pd.api.types.is_numeric_dtype(df[col]):
            feature_table[col] = 'numerical'
        else:
            feature_table[col] = 'other' 
    
    return feature_table

def create_summary_table(df):
    summary = []
    
    for col in df.columns:
        col_name = col
        dtype = df[col].dtype
        unique_count = df[col].nunique()
        missing_count = df[col].isnull().sum()
        summary.append([col_name, dtype, unique_count, missing_count])
        
    summary_df = pd.DataFrame(summary, columns=['Column Name', 'Data Type', 'Unique Values', 'Missing Values'])
    
    return summary_df

def drop_NAN(df):
    df_no_null = df.dropna()
    return df_no_null 

def missing_values_percent(df):
    if find_null(df).sum() > 0:
        nan_percentage = (find_null(df).sum() / len(df)) * 100
        return nan_percentage

def get_numerical_columns(df):
    return df.select_dtypes(include=['number']).columns

def get_categorical_columns(df):
    return df.select_dtypes(include=['object', 'category']).columns

def handle_missing_values(df):
    numerical_cols = get_numerical_columns(df)
    categorical_cols = get_categorical_columns(df)
    if missing_values_percent(df) < 1:
        df = df.dropna()
    else:
        df.loc[:, numerical_cols] = df.loc[:, numerical_cols].fillna(df[numerical_cols].mean())
        
        for col in categorical_cols:
            df.loc[:, col] = df[col].fillna(df[col].mode().iloc[0])
    
    return df

def export_csv(df, output_filepath):
    df.to_csv(output_filepath, index=False)
    return f'File saved at {output_filepath}'

# Main script
file_path = 'sample-synthetic-healthcare.csv'
output_filepath = 'sample-synthetic-healthcare-cleaned.csv'

# Load the dataset
df = load_csv(file_path)
original_shape = check_shape(df)

# Reshape the data if necessary
df_reshape = reshape_data(df)

# Create a summary table
summary_table = create_summary_table(df_reshape)

# Calculate percentage of missing values
nan_percentage = missing_values_percent(df_reshape)

# Handle missing values
cleaned_data = handle_missing_values(df_reshape)

# Export the cleaned data to a CSV file
export_message = export_csv(cleaned_data, output_filepath)

# Print results
print(f'Total data shape: {original_shape}')
print(f'We will take only 5k rows, reshaped data shape: {df_reshape.shape}')
print(f'Null values: {find_null(df_reshape).sum()}')
print(f'NaN percentage: {nan_percentage}')
print(summary_table)
print(cleaned_data.head(10))
print(export_message)
print(f'Cleaned data shape: {cleaned_data.shape}')
