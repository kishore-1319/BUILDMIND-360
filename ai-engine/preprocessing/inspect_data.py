import pandas as pd

FILES = [
    "data/raw/Instagram.csv",
    "data/raw/WhatsApp.csv"
]

for file in FILES:

    print("\n====================================")
    print(f"INSPECTING: {file}")
    print("====================================")

    df = pd.read_csv(file)

    print("\n1. Number of reviews:")
    print(len(df))

    print("\n2. Columns:")
    print(df.columns.tolist())

    print("\n3. First 5 rows:")
    print(df.head())

    print("\n4. Missing values:")
    print(df.isna().sum())

    print("\n5. Duplicate review IDs:")
    print(df["reviewId"].duplicated().sum())

    print("\n6. Duplicate review text:")
    print(df["content"].duplicated().sum())

    print("\n7. Rating values:")
    print(sorted(df["score"].dropna().unique()))

    print("\n8. Data types:")
    print(df.dtypes)
