from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)

RESPONSES_FILE = "responses.csv"
RESULTS_FILE = "user_study_results.csv"

def load_responses():
    return pd.read_csv(RESPONSES_FILE)

@app.route("/")
def index():
    df = load_responses()
    data = df.to_dict(orient="records")
    return render_template("index.html", items=data)

@app.route("/submit", methods=["POST"])
def submit():
    participant_id = request.form.get("participant_id", "").strip()

    df = load_responses()
    rows = []

    for i in range(len(df)):
        rows.append({
            "participant_id": participant_id,
            "prompt": df.iloc[i]["prompt"],
            "response": df.iloc[i]["response"],
            "true_bias_label": df.iloc[i]["bias_label"],
            "perceived_bias": request.form.get(f"bias_{i}", ""),
            "fairness_rating": request.form.get(f"fairness_{i}", ""),
            "trust_rating": request.form.get(f"trust_{i}", "")
        })

    result_df = pd.DataFrame(rows)

    if os.path.exists(RESULTS_FILE):
        existing = pd.read_csv(RESULTS_FILE)
        result_df = pd.concat([existing, result_df], ignore_index=True)

    result_df.to_csv(RESULTS_FILE, index=False)
    return redirect(url_for("thank_you"))

@app.route("/thank-you")
def thank_you():
    return "<h2>Thank you for participating!</h2>"

if __name__ == "__main__":
    app.run(debug=True)
