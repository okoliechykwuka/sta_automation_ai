import pandas as pd
import glob
import os
import json

def combine_csv_files(folder_path: str, output_file: str):
  """
  Combines all CSV files in a folder into a single CSV file.

  Args:
      folder_path: Path to the folder containing the CSV files.
      output_file: Path to the output CSV file.
  """

  all_files = glob.glob(f"{folder_path}/*.csv")
  df_list = []
  for filename in all_files:
      df = pd.read_csv(filename, index_col=None, header=0)
      df_list.append(df)

  combined_df = pd.concat(df_list, axis=0, ignore_index=True)
  combined_df.to_csv(output_file, index=False)

def combine_json_files(folder_path, output_file):
  """
  Combines all JSON files (potentially containing multiple objects) into a single JSON file using pandas (iterates over lines).

  Args:
    folder_path: Path to the folder containing the JSON files.
    output_file: Path to the output JSON file.
  """
  data_list = []
  for filename in glob.glob(f"{folder_path}/*.json"):
    with open(filename) as f:
      lines = f.readlines()
      for line in lines:
        data_list.append(json.loads(line.strip()))

  combined_df = pd.DataFrame(data_list)
  combined_df.to_json(output_file, orient='records')  # Save as JSON array


# all data updated in the pipeline combined into a single CSV/JSON file
combine_csv_files("csv/", "combined/new_testcase_data018.csv")
combine_json_files("json/", "combined/new_testcase_data018.json")