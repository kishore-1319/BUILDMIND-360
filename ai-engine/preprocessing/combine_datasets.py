from pathlib import Path

import pandas as pd


PROCESSED_FOLDER = Path("data/processed")
OUTPUT_FILE = PROCESSED_FOLDER / "master_feedback.csv"


def combine_datasets():

    instagram_file = PROCESSED_FOLDER / "Instagram_processed.csv"
    whatsapp_file = PROCESSED_FOLDER / "WhatsApp_processed.csv"

    print("Loading processed datasets...")

    instagram = pd.read_csv(instagram_file)
    whatsapp = pd.read_csv(whatsapp_file)

    print(f"Instagram rows: {len(instagram)}")
    print(f"WhatsApp rows: {len(whatsapp)}")

    # Remember where each review came from
    instagram["source"] = "Instagram"
    whatsapp["source"] = "WhatsApp"

    # Combine both datasets
    master = pd.concat(
        [instagram, whatsapp],
        ignore_index=True
    )

    # Save master dataset
    master.to_csv(
        OUTPUT_FILE,
        index=False,
        encoding="utf-8"
    )

    print("\n==============================")
    print("MASTER DATASET CREATED")
    print("==============================")

    print(f"Total rows: {len(master)}")
    print(f"Instagram rows: {(master['source'] == 'Instagram').sum()}")
    print(f"WhatsApp rows: {(master['source'] == 'WhatsApp').sum()}")

    print(f"\nSaved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    combine_datasets()