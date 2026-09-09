from pathlib import Path

import pandas as pd

from preprocessing.cleaner import clean_text


RAW_FOLDER = Path("data/raw")
PROCESSED_FOLDER = Path("data/processed")


def process_file(input_file):
    print("\n====================================")
    print(f"PROCESSING: {input_file.name}")
    print("====================================")

    # Read original CSV
    df = pd.read_csv(input_file)

    print(f"Original rows: {len(df)}")

    # Keep the original customer review
    df["raw_content"] = df["content"]

    # Handle truly empty content
    df["content"] = df["content"].fillna("")

    # Clean the review text
    df["cleaned_content"] = df["content"].apply(clean_text)

    # Check whether review is empty
    df["is_empty"] = df["cleaned_content"].str.strip().eq("")

    # Check very short reviews
    df["is_very_short"] = df["cleaned_content"].str.len().le(2)

    # Flag repeated review text
    df["is_duplicate_content"] = (
        df["cleaned_content"].duplicated(keep=False)
    )

    # Check whether rating is valid
    df["valid_score"] = df["score"].isin([1, 2, 3, 4, 5])

    # Default status
    df["processing_status"] = "accepted"

    # Empty reviews are rejected
    df.loc[
        df["is_empty"],
        "processing_status"
    ] = "rejected_empty"

    # Create processed folder if needed
    PROCESSED_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    # Output file
    output_file = (
        PROCESSED_FOLDER
        / f"{input_file.stem}_processed.csv"
    )

    # Save processed data
    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8"
    )

    # Show results
    print("\nRESULT")
    print("------------------------------------")
    print(f"Total rows: {len(df)}")
    print(f"Empty reviews: {df['is_empty'].sum()}")
    print(f"Very short reviews: {df['is_very_short'].sum()}")
    print(
        f"Duplicate review texts: "
        f"{df['is_duplicate_content'].sum()}"
    )
    print(
        f"Invalid ratings: "
        f"{(~df['valid_score']).sum()}"
    )
    print(
        f"Accepted reviews: "
        f"{(df['processing_status'] == 'accepted').sum()}"
    )
    print(f"Saved to: {output_file}")


def main():

    files = list(
        RAW_FOLDER.glob("*.csv")
    )

    if not files:
        print("No CSV files found in data/raw/")
        return

    for file in files:
        process_file(file)


if __name__ == "__main__":
    main()