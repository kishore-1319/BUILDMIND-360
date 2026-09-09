import pandas as pd

FILE = "data/processed/master_feedback_ready.csv"


def final_check():
    df = pd.read_csv(FILE)

    print("\n========== FINAL DATASET CHECK ==========\n")

    # 1. Total records
    print("Total records:", len(df))

    # 2. Required columns
    required_columns = [
        "reviewId",
        "content",
        "score",
        "raw_content",
        "cleaned_content",
        "is_empty",
        "is_very_short",
        "is_duplicate_content",
        "valid_score",
        "processing_status",
        "source",
        "llm_ready"
    ]

    print("\n--- Required Columns ---")

    missing_columns = [
        column for column in required_columns
        if column not in df.columns
    ]

    if not missing_columns:
        print("All required columns are present.")
    else:
        print("Missing columns:", missing_columns)

    # 3. Duplicate review IDs
    print("\n--- Duplicate Review IDs ---")
    print("Duplicate IDs:", df["reviewId"].duplicated().sum())

    # 4. Invalid scores
    print("\n--- Invalid Scores ---")
    print("Invalid scores:", (~df["score"].isin([1, 2, 3, 4, 5])).sum())

    # 5. LLM readiness
    print("\n--- LLM Readiness ---")
    print("LLM ready:", df["llm_ready"].sum())
    print("Not ready:", (~df["llm_ready"]).sum())

    # 6. Empty reviews
    print("\n--- Empty Reviews ---")
    print("Empty reviews:", df["is_empty"].sum())

    # 7. Sources
    print("\n--- Sources ---")
    print(df["source"].value_counts())

    print("\n=========================================")

    # Final decision
    if (
        not missing_columns
        and df["reviewId"].duplicated().sum() == 0
        and (~df["score"].isin([1, 2, 3, 4, 5])).sum() == 0
    ):
        print("FINAL CHECK: PASSED ✅")
        print("Dataset is ready for the LLM stage.")
    else:
        print("FINAL CHECK: FAILED ❌")
        print("Please fix the problems above.")


if __name__ == "__main__":
    final_check()