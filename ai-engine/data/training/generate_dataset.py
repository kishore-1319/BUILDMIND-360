import json
import pandas as pd
import torch

from llm.model import load_model
from llm.prompts import SYSTEM_PROMPT


INPUT_FILE = "data/processed/clean_feedback.csv"
OUTPUT_FILE = "data/training/generated_dataset.jsonl"


def build_labeling_prompt(feedback: str) -> str:

    return f"""
{SYSTEM_PROMPT}

You are creating a training example for BUILDMIND-360.

Analyze the customer feedback below.

CUSTOMER FEEDBACK:
{feedback}

Return ONLY valid JSON with exactly these fields:

{{
    "summary": "",
    "customer_problem": "",
    "affected_feature": "",
    "issue": "",
    "sentiment": "",
    "intent": "",
    "severity": "",
    "customer_impact": "",
    "business_impact": "",
    "root_cause_hypothesis": "",
    "evidence": [],
    "priority": "",
    "recommended_solution": "",
    "development_action": "",
    "product_action": "",
    "engineering_action": "",
    "support_action": "",
    "expected_outcome": "",
    "confidence": 0.0
}}

Important rules:

- Only use information supported by the feedback.
- Root cause must be a hypothesis, not a claimed fact.
- Do not invent technical details.
- If information is unknown, say "Unknown".
- The solution must be practical.
- Development action must answer: "What should the company develop or change next?"
- Return JSON only.
"""


def extract_json(text: str):

    start = text.find("{")
    end = text.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("No JSON object found in model output.")

    return json.loads(text[start:end + 1])


def generate_dataset():

    print("Loading cleaned feedback...")

    df = pd.read_csv(INPUT_FILE)

    print(f"Feedback records: {len(df)}")

    tokenizer, model = load_model()

    device = next(model.parameters()).device

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as output_file:

        for index, row in df.iterrows():

            feedback = str(row["cleaned_content"]).strip()

            if not feedback:
                continue

            print(
                f"\nProcessing {index + 1}/{len(df)}"
            )

            messages = [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": build_labeling_prompt(feedback)
                }
            ]

            prompt = tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True,
                enable_thinking=False
            )

            inputs = tokenizer(
                prompt,
                return_tensors="pt"
            )

            inputs = {
                key: value.to(device)
                for key, value in inputs.items()
            }

            with torch.no_grad():

                outputs = model.generate(
                    **inputs,
                    max_new_tokens=300,
                    do_sample=False,
                    pad_token_id=tokenizer.eos_token_id
                )

            generated_tokens = outputs[0][
                inputs["input_ids"].shape[1]:
            ]

            raw_output = tokenizer.decode(
                generated_tokens,
                skip_special_tokens=True
            ).strip()

            try:

                analysis = extract_json(raw_output)

                training_example = {
                    "input": feedback,
                    "output": analysis
                }

                output_file.write(
                    json.dumps(
                        training_example,
                        ensure_ascii=False
                    ) + "\n"
                )

                output_file.flush()

                print("✓ Generated successfully")

            except Exception as error:

                print(
                    f"✗ Failed: {error}"
                )

    print("\n==============================")
    print("DATASET GENERATION COMPLETE")
    print("==============================")
    print(f"Saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    generate_dataset()