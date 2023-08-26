import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Read the input text file
with open("input.txt") as f:
    data = f.read()

# Split the data into code snippets and labels
code_snippets = data.split("\n")
labels = [
    "optimize" if "optimize" in snippet else "ok" for snippet in code_snippets
]

# Convert the code snippets into numerical features
vectorizer = TfidfVectorizer(
    tokenizer=lambda x: x.split(), stop_words=None, max_features=5000, ngram_range=(1, 2)
)
X = vectorizer.fit_transform(code_snippets)

# Train a RandomForestClassifier model
model = RandomForestClassifier(
    n_estimators=100, max_depth=10, random_state=42, min_samples_split=2, min_samples_leaf=1
)
model.fit(X, labels)

# Predict the suggested improvement for each code snippet
predictions = model.predict(X)

# Print the results
for i, (code_snippet, prediction) in enumerate(zip(code_snippets, predictions)):
    print(f"Code snippet {i + 1}: {code_snippet}")
    print(f"Suggested improvement: {prediction}")
