# data_operations.py

import pandas as pd
from classified_dataframe import ClassifiedDataFrame

def process_data_with_classifications(csv_file_path, json_file_path):
    # Read CSV file into ClassifiedDataFrame
    data = ClassifiedDataFrame(pd.read_csv(csv_file_path))

    # Load classifications from JSON file
    data = data.load_classifications_from_json(json_file_path)

    # Example operations (modify as per your requirements)
    numeric_data = get_numeric_data(data)
    categorical_data = get_categorical_data(data)

    # Combine results into a single DataFrame for export
    combined_data = pd.concat([numeric_data, categorical_data], axis=1)

    # Export combined_data to CSV or other formats
    combined_data.to_csv('combined_data.csv', index=False)

def get_numeric_data(data):
    numeric_columns = data.classifications['Numeric Data']
    return data[numeric_columns]

def get_categorical_data(data):
    categorical_columns = data.classifications['Categorical Data']
    return data[categorical_columns]
