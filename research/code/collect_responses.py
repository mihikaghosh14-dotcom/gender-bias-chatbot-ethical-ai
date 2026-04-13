

import csv
import os
from datetime import datetime

INPUT_PATH = os.path.join("research", "data", "prompts.csv")
OUTPUT_PATH = os.path.join("research", "data", "responses.csv")


def load_prompts():
    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def generate_placeholder_response(prompt_text: str, model_name: str) -> str:
    return f"[PLACEHOLDER RESPONSE from {model_name}] {prompt_text}"


def main() -> None:
    prompts = load_prompts()
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    model_names = ["GPT-4", "Claude", "Gemini"]
    rows = []

    for prompt in prompts:
        for model_name in model_names:
            rows.append({
                "prompt_id": prompt["prompt_id"],
                "base_prompt_id": prompt["base_prompt_id"],
                "gender": prompt["gender"],
                "model_name": model_name,
                "prompt_text": prompt["prompt_text"],
                "response_text": generate_placeholder_response(prompt["prompt_text"], model_name),
                "timestamp": datetime.utcnow().isoformat()
            })

    with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "prompt_id",
                "base_prompt_id",
                "gender",
                "model_name",
                "prompt_text",
                "response_text",
                "timestamp"
            ]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved {len(rows)} responses to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()