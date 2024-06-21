# main.py

import pandas as pd
from data_operations import process_data_with_classifications

def main():
    csv_file_path = 'sample_data.csv'
    json_file_path = 'classifications.json'

    # Process data with classifications
    process_data_with_classifications(csv_file_path, json_file_path)

if __name__ == "__main__":
    main()
