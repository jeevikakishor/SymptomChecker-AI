import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("dataset.csv")

X = data.drop("disease", axis=1)
y = data["disease"]

encoder = LabelEncoder()

for col in X.columns:
    X[col] = encoder.fit_transform(X[col])

model = RandomForestClassifier()
model.fit(X, y)

def predict_disease(symptoms):

    input_data = [symptoms]

    probabilities = model.predict_proba(input_data)[0]

    diseases = model.classes_

    results = sorted(
        zip(diseases, probabilities),
        key=lambda x: x[1],
        reverse=True
    )

    return results[:3]