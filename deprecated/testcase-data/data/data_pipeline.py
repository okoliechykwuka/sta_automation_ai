import pandas as pd
import json

class TestCasePipeline:
    def __init__(self):
        self.dataframes = []

    def add_dataframe(self, df):
        """Add a dataframe to the pipeline."""
        self.dataframes.append(df)

    def combine_dataframes(self):
        """Combine all dataframes into a single dataframe."""
        if not self.dataframes:
            raise ValueError("No dataframes to combine")
        return pd.concat(self.dataframes, ignore_index=True)

    def to_json(self, combined_df, filepath):
        """Save the combined dataframe to a JSON file."""
        json_data = combined_df.to_json(orient='records', lines=True)
        with open(filepath, 'w') as file:
            file.write(json_data)
        return filepath

    def json_to_csv(self, json_filepath, csv_filepath):
        """Convert a JSON file to CSV format."""
        df_from_json = pd.read_json(json_filepath, orient='records', lines=True)
        df_from_json.to_csv(csv_filepath, index=False)
        return csv_filepath
