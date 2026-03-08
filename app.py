import os
from flask import Flask, render_template, request
from model import predict_disease

app = Flask(__name__)

symptoms = [
"fever","cough","headache","vomiting","stomach_pain",
"nausea","fatigue","chills","joint_pain","muscle_pain"
]

precautions = {
"Flu": ["Drink warm fluids","Take rest","Use paracetamol"],
"Food Poisoning": ["Drink ORS","Avoid oily food","Stay hydrated"],
"Allergy": ["Avoid allergens","Take antihistamines","Consult doctor"]
}

@app.route("/", methods=["GET","POST"])
def home():

    predictions = None
    advice = None

    if request.method == "POST":

        s1 = request.form["symptom1"]
        s2 = request.form["symptom2"]
        s3 = request.form["symptom3"]

        predictions = predict_disease([s1,s2,s3])

        disease = predictions[0][0]

        advice = precautions.get(disease,["Consult a doctor"])

    return render_template(
        "index.html",
        symptoms=symptoms,
        predictions=predictions,
        advice=advice
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
