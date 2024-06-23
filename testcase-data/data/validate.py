import pandas as pd

path = "combined/all_combined_testcase_data023.csv"
df = pd.read_csv(path)

print(df.shape)
# print(df)
print(df.columns)