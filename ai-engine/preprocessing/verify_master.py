import pandas as pd


FILE = "data/processed/master_feedback.csv"


print("Loading master dataset...")

df = pd.read_csv(FILE)


print("\n==============================")
print("MASTER DATASET CHECK")
print("==============================")


print("\n1. Total rows:")
print(len(df))


print("\n2. Columns:")
print(df.columns.tolist())


print("\n3. Source counts:")
print(df["source"].value_counts())


print("\n4. Missing values:")
print(df.isna().sum())


print("\n5. Duplicate review IDs:")
print(df["reviewId"].duplicated().sum())


print("\n6. Score values:")
print(sorted(df["score"].dropna().unique()))


print("\n7. First 5 rows:")
print(df.head())


print("\n==============================")
print("CHECK COMPLETE")
print("==============================")