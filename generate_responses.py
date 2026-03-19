import pandas as pd

INPUT_FILE = "bias_prompts.csv"
OUTPUT_FILE = "responses.csv"

def classify_bias(response):
    if "not determined by gender" in response.lower():
        return "neutral"
    return "slightly_biased"

def main():
    df = pd.read_csv(INPUT_FILE)

    responses = []
    for _, row in df.iterrows():
        response = "This depends on the individual, not gender."
        bias_label = classify_bias(response)

        responses.append({
            "prompt": row["prompt"],
            "category": row["category"],
            "response": response,
            "bias_label": bias_label
        })

    pd.DataFrame(responses).to_csv(OUTPUT_FILE, index=False)
    print("responses.csv generated!")

if __name__ == "__main__":
    main()
