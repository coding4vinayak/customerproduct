# classified_dataframe.py

import pandas as pd
import json

class ClassifiedDataFrame(pd.DataFrame):
    _metadata = ['classifications']

    def classify_columns(self):
        classifications = {
            'Integer Data': [],
            'Float Data': [],
            'Numeric Data': [],
            'Categorical Data': [],
            'Binary Data': [],
            'Email Data': [],
            'Temporal Data': [],
            'Spatial Data': [],
            'ID Data': []  # Example for ID data
        }

        for col in self.columns:
            dtype = self[col].dtype

            if pd.api.types.is_integer_dtype(dtype):
                unique_values = self[col].nunique()
                if unique_values == 2:
                    classifications['Binary Data'].append(col)
                classifications['Integer Data'].append(col)
                classifications['Numeric Data'].append(col)
            elif pd.api.types.is_float_dtype(dtype):
                classifications['Float Data'].append(col)
                classifications['Numeric Data'].append(col)
            elif pd.api.types.is_object_dtype(dtype):
                if self[col].str.contains('@').all():
                    classifications['Email Data'].append(col)
                else:
                    classifications['Categorical Data'].append(col)
            elif pd.api.types.is_datetime64_any_dtype(dtype):
                classifications['Temporal Data'].append(col)
            elif dtype.name == 'geometry':
                classifications['Spatial Data'].append(col)
            elif any(substring in col.lower() for substring in ['id', 'num', 'code']):
                classifications['ID Data'].append(col)

        self.classifications = classifications

    def export_classifications_to_json(self, json_file_path):
        with open(json_file_path, 'w') as f:
            json.dump(self.classifications, f)

    @classmethod
    def load_classifications_from_json(cls, json_file_path):
        with open(json_file_path, 'r') as f:
            classifications = json.load(f)
        instance = cls()
        instance.classifications = classifications
        return instance
