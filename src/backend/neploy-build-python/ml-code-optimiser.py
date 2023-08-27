import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Sample dataset containing smart contract code snippets and labels indicating improvement needs
data = [
    ("function transfer(address _to, uint256 _value) public returns (bool) { ... }", "optimize"),
    ("for (uint256 i = 0; i < n; i++) { ... }", "optimize"),
    ("mapping(address => uint256) balances;", "ok"),
    # ... more data ...
]

# Convert data to DataFrame
df = pd.DataFrame(data, columns=["code", "label"])

# Preprocessing: Convert code snippets into numerical features using CountVectorizer
vectorizer = CountVectorizer(ngram_range=(1, 2))
X = vectorizer.fit_transform(df["code"])
y = df["label"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier (you can use more advanced models as well)
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
#print(classification_report(y_test, y_pred))

# Read the file containing the Python smart contract script
with open("test.py", "r") as f:
  code = f.read()

# Split the code into lines
lines = code.split("\n")

# Predict the improvement suggestions for each line of code
for i, line in enumerate(lines):
  new_code_vectorized = vectorizer.transform([line])
  prediction = model.predict(new_code_vectorized)[0]

  # Print the improvement suggestions
  if not lines[i]:
    print("{}".format(lines[i]))
    continue
  if prediction == "optimize":
    print("[optimised]: {}".format(lines[i]))
    #for snippet in model.predict_proba(new_code_vectorized)[0]:
    #  print(snippet)
  else:
    print("[    ok   ]: {}".format(lines[i]))
