

import csv
import os
from collections import defaultdict

INPUT_PATH = os.path.join("research", "data", "responses.csv")
OUTPUT_PATH = os.path.join("research", "data", "analysis_summary.csv")

POSITIVE_WORDS = {
    "strong", "confident", "capable", "effective", "intelligent",
    "excellent", "skilled", "qualified", "successful", "talented"
}

DESCRIPTIVE_WORDS = {
    "strong", "confident", "capable", "effective", "intelligent",
    "calm", "supportive", "ambitious", "thoughtful", "reliable",
    "creative", "analytical", "organized", "kind", "assertive"
}


def simple_sentiment_score(text: str) -> float:
    words = text.lower().split()
    if not words:
        return 0.0
    hits = sum(1 for word in words if word.strip(".,!?;:") in POSITIVE_WORDS)
    return round(hits / len(words), 4)


def word_count(text: str) -> int:
    return len(text.split())


def descriptive_count(text: str) -> int:
    words = text.lower().split()
    return sum(1 for word in words if word.strip(".,!?;:") in DESCRIPTIVE_WORDS)


def main() -> None:
    if not os.path.exists(INPUT_PATH):
        print(f"Missing file: {INPUT_PATH}")
        return

    grouped = defaultdict(lambda: {
        "sentiment_total": 0.0,
        "length_total": 0,
        "descriptive_total": 0,
        "count": 0
    })

    with open(INPUT_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            gender = row["gender"]
            response_text = row["response_text"]

            grouped[gender]["sentiment_total"] += simple_sentiment_score(response_text)
            grouped[gender]["length_total"] += word_count(response_text)
            grouped[gender]["descriptive_total"] += descriptive_count(response_text)
            grouped[gender]["count"] += 1

    summary_rows = []
    for gender, stats in grouped.items():
        count = stats["count"]
        if count == 0:
            continue

        summary_rows.append({
            "gender": gender,
            "avg_sentiment_score": round(stats["sentiment_total"] / count, 4),
            "avg_response_length": round(stats["length_total"] / count, 2),
            "avg_descriptive_frequency": round(stats["descriptive_total"] / count, 2),
            "num_responses": count
        })

    with open(OUTPUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "gender",
                "avg_sentiment_score",
                "avg_response_length",
                "avg_descriptive_frequency",
                "num_responses"
            ]
        )
        writer.writeheader()
        writer.writerows(summary_rows)

    print(f"Saved analysis summary to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()