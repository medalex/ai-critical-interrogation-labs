from transformers import pipeline
import pandas as pd

classifier = pipeline("sentiment-analysis")
data = pd.read_csv("bias_inputs.csv")

for text in data["Text"]:
    result = classifier(text)[0]
    print(text, result)
