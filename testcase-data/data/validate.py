import pandas as pd

path = "data/combined/testcaseKeywords.csv"
df = pd.read_csv(path)

print(df.shape)
print(df)
