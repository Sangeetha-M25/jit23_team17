import pandas as pd

con = pd.read_csv("Dataset/CON1/CON1.csv")
rel = pd.read_csv("Dataset/RELAXED1/RELAXED1.csv")

print("=" * 50)
print("CONCENTRATION DATA")
print("=" * 50)
print(con.head())

print("\nColumns:")
print(con.columns)

print("\nShape:")
print(con.shape)

print("\n" + "=" * 50)
print("RELAXED DATA")
print("=" * 50)
print(rel.head())

print("\nColumns:")
print(rel.columns)

print("\nShape:")
print(rel.shape)