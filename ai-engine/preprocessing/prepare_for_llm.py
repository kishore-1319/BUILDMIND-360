import pandas as pd


INPUT_FILE = "data/processed/master_feedback.csv"
OUTPUT_FILE = "data/processed/master_feedback_ready.csv"


def prepare_dataset():

    print("Loading master dataset...")

    df = pd.read_csv(INPUT_FILE)

    # A review is ready if it has actual content
    # and a valid rating.
    df["llm_ready"] = (
        (~df["is_empty"])
        & (df["valid_score"])
    )

    # Save the new dataset
    df.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8"
    )

    print("\n==============================")
    print("LLM READINESS CHECK")
    print("==============================")

    print(f"Total reviews: {len(df)}")

    print(
        f"LLM ready: "
        f"{df['llm_ready'].sum()}"
    )

    print(
        f"Not ready: "
        f"{(~df['llm_ready']).sum()}"
    )

    print(f"\nSaved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    prepare_dataset()