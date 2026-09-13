import pandas as pd

df = pd.read_csv("data/Tesla.csv")

print("Rows:", len(df))
print("Columns:", list(df.columns))
print("\nFirst 5 posts:")
print(df.head())