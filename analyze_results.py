import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("user_study_results.csv")

print("Average fairness:", df["fairness_rating"].astype(float).mean())
print("Average trust:", df["trust_rating"].astype(float).mean())

df["perceived_bias"].value_counts().plot(kind="bar")
plt.title("User Bias Perception")
plt.savefig("bias_chart.png")
plt.show()
