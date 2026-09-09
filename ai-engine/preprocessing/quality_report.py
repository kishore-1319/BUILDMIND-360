import pandas as pd

FILE = "data/processed/master_feedback_ready.csv"


def generate_quality_report():
    df = pd.read_csv(FILE)

    print("\n========== DATASET QUALITY REPORT ==========\n")

    # Basic information
    print("Total reviews:", len(df))

    # Source distribution
    print("\n--- Source Distribution ---")
    print(df["source"].value_counts())

    # LLM readiness
    print("\n--- LLM Readiness ---")
    print(df["llm_ready"].value_counts())

    # Missing values
    print("\n--- Missing Values ---")
    print(df.isnull().sum())

    # Duplicate content flags
    print("\n--- Duplicate Content Flags ---")
    print(df["is_duplicate_content"].value_counts())

    # Very short reviews
    print("\n--- Very Short Review Flags ---")
    print(df["is_very_short"].value_counts())

    # Empty reviews
    print("\n--- Empty Review Flags ---")
    print(df["is_empty"].value_counts())

    # Rating distribution
    print("\n--- Rating Distribution ---")
    print(df["score"].value_counts().sort_index())

    print("\n============================================")
    print("Quality report completed successfully.")


if __name__ == "__main__":
    generate_quality_report()