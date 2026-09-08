import json
import time
import torch

from llm.model import load_model
from llm.prompts import SYSTEM_PROMPT
from schemas.feedback_analysis import FeedbackAnalysis


def analyze_feedback(feedback: str):

    tokenizer, model = load_model()

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": f"""
Analyze the following customer feedback.

CUSTOMER FEEDBACK:
{feedback}

Return JSON with exactly these fields:

{{
    "summary": "",
    "customer_problem": "",
    "affected_feature": "",
    "issue": "",
    "sentiment": "",
    "intent": "",
    "severity": "",
    "customer_impact": "",
    "business_impact": null,
    "root_cause_hypothesis": null,
    "evidence": [],
    "priority": "",
    "recommended_solution": "",
    "development_action": "",
    "product_action": null,
    "engineering_action": null,
    "support_action": null,
    "expected_outcome": null,
    "confidence": 0.0
}}
"""
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

    device = next(model.parameters()).device

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    start_time = time.time()

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

    raw_result = tokenizer.decode(
        generated_tokens,
        skip_special_tokens=True
    ).strip()

    elapsed = time.time() - start_time

    print(f"Generation time: {elapsed:.2f} seconds")

    # Try to extract JSON
    try:

        data = json.loads(raw_result)

    except json.JSONDecodeError:

        start = raw_result.find("{")
        end = raw_result.rfind("}")

        if start == -1 or end == -1:
            raise ValueError(
                "Model did not return valid JSON.\n"
                f"Raw output:\n{raw_result}"
            )

        data = json.loads(
            raw_result[start:end + 1]
        )

    # Validate against our schema
    analysis = FeedbackAnalysis.model_validate(data)

    return analysis