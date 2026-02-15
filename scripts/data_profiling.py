import pandas as pd

file_path = "../data/raw/Superstore.csv"
df = pd.read_csv(file_path, encoding='latin1')

print("First 5 rows:")
print(df.head())

print("\nData Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())