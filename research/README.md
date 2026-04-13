

# Gender Bias in AI Chatbots – Research Code

This folder contains the experimental pipeline used for Project Update 2.

## Files

### `code/generate_prompts.py`
Creates controlled male, female, and gender-neutral prompt variations and saves them to `data/prompts.csv`.

### `code/collect_responses.py`
Creates a structured response file for the evaluated models and saves it to `data/responses.csv`.

### `code/analyze_results.py`
Computes simple comparison metrics including:
- sentiment score
- response length
- descriptive language frequency

Results are saved to `data/analysis_summary.csv`.

## Data files

- `data/prompts.csv`
- `data/responses.csv`
- `data/analysis_summary.csv`

## Notes
This code supports the methodology described in Project Update 2 and is intended to organize prompt generation, response collection, and preliminary analysis.