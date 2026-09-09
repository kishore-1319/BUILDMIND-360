import pandas as pd

from preprocessing.cleaner import clean_text


INPUT_FILE = "data/raw/feedback.csv"
OUTPUT_FILE = "data/processed/clean_feedback.csv"


def process_dataset():

    print("Loading dataset...")

    df = pd.read_csv(INPUT_FILE)

    print(f"Records loaded: {len(df)}")

    # Clean feedback text
    df["cleaned_content"] = (
        df["content"]
        .fillna("")
        .apply(clean_text)
    )

    # Remove records where content is empty
    df = df[df["cleaned_content"].str.strip() != ""]

    # Remove duplicate feedback
    df = df.drop_duplicates(
        subset=["cleaned_content"]
    )

    # Save processed dataset
    df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(
        f"Processed records: {len(df)}"
    )

    print(
        f"Saved to: {OUTPUT_FILE}"
    )


if __name__ == "__main__":
    process_dataset()