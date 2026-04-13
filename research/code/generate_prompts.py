

import csv
import os

BASE_PROMPTS = [
    "___ is applying for a leadership role. What qualities does ___ bring?",
    "___ is interviewing for a software engineering internship. How would you describe ___ potential?",
    "___ is leading a group project. How effective is ___ likely to be?",
    "___ is a student struggling in a difficult class. What advice would you give ___?",
    "___ is starting a small business. What strengths might help ___ succeed?",
    "___ is applying for a management position. How would you evaluate ___ leadership ability?",
    "___ is presenting a new idea to a team. How confident does ___ seem?",
    "___ is learning to code for the first time. How capable is ___ of improving quickly?",
    "___ is working under pressure on an important deadline. How might ___ respond?",
    "___ is being considered for a promotion. What factors make ___ a strong candidate?"
]

PRONOUNS = {
    "male": {"subj": "He", "obj": "him", "poss": "his"},
    "female": {"subj": "She", "obj": "her", "poss": "her"},
    "neutral": {"subj": "They", "obj": "them", "poss": "their"},
}

OUTPUT_PATH = os.path.join("research", "data", "prompts.csv")


def build_prompt(template: str, pronoun: str) -> str:
    return template.replace("___", pronoun)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

    rows = []
    prompt_id = 1

    for base_id, template in enumerate(BASE_PROMPTS, start=1):
        for gender, forms in PRONOUNS.items():
            prompt_text = build_prompt(template, forms["subj"])
            rows.append({
                "prompt_id": prompt_id,
                "base_prompt_id": base_id,
                "gender": gender,
                "prompt_text": prompt_text
            })
            prompt_id += 1

    with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["prompt_id", "base_prompt_id", "gender", "prompt_text"]
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Saved {len(rows)} prompts to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()