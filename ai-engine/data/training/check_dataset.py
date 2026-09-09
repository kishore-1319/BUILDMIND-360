import json


FILE = "data/training/train.jsonl"


def check_dataset():

    valid = 0
    invalid = 0

    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as f:

        for line_number, line in enumerate(
            f,
            start=1
        ):

            line = line.strip()

            if not line:
                continue

            try:
                item = json.loads(line)

                if "input" not in item:
                    raise ValueError("Missing input")

                if "output" not in item:
                    raise ValueError("Missing output")

                valid += 1

            except Exception as e:

                invalid += 1

                print(
                    f"Line {line_number}: {e}"
                )

    print("\n==========================")
    print("DATASET CHECK")
    print("==========================")
    print(f"Valid examples: {valid}")
    print(f"Invalid examples: {invalid}")


if __name__ == "__main__":
    check_dataset()