import json


FILE = "data/training/generate_dataset.py"


def check_dataset():

    valid = 0
    invalid = 0

    with open(
        FILE,
        "r",
        encoding="utf-8"
    ) as file:

        for line_number, line in enumerate(
            file,
            start=1
        ):

            line = line.strip()

            if not line:
                continue

            try:

                item = json.loads(line)

                required_fields = [
                    "input",
                    "output"
                ]

                for field in required_fields:

                    if field not in item:
                        raise ValueError(
                            f"Missing field: {field}"
                        )

                valid += 1

            except Exception as error:

                invalid += 1

                print(
                    f"Line {line_number}: {error}"
                )

    print("\n==============================")
    print("GENERATED DATASET CHECK")
    print("==============================")
    print(f"Valid examples: {valid}")
    print(f"Invalid examples: {invalid}")


if __name__ == "__main__":
    check_dataset()