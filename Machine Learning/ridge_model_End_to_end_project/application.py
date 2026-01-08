from flask import Flask, request, jsonify
import pickle
import numpy as np
import os
from flask import Flask, render_template
application = Flask(__name__)
app=application

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# MODEL_DIR = os.path.join(BASE_DIR, "models")

with open(os.path.join(BASE_DIR, "scaler.pkl"), "rb") as f:
    standard_scaler = pickle.load(f)

with open(os.path.join(BASE_DIR, "ridge_model.pkl"), "rb") as f:
    ridge_model = pickle.load(f)

# print("Scaler loaded:", type(standard_scaler))
# print("Model loaded:", type(ridge_model))



# -----------------------
# Health check
# -----------------------
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict_data", methods=["GET","POST"])
def predict():
    if request.method == "POST":
        # 1. Read form data
        Temperature = float(request.form["Temperature"])
        RH = float(request.form["RH"])
        Ws = float(request.form["Ws"])
        Rain = float(request.form["Rain"])
        FFMC = float(request.form["FFMC"])
        DMC = float(request.form["DMC"])
        ISI = float(request.form["ISI"])
        Classes = float(request.form["Classes"])
        Region = float(request.form["Region"])

        # 2. Arrange input in SAME order as training
        input_data = np.array([[ 
            Temperature, RH, Ws, Rain,
            FFMC, DMC, ISI, Classes, Region
        ]])
        # 3. Scale the input
        scaled_data = standard_scaler.transform(input_data)

        # 4. Predict
        prediction = ridge_model.predict(scaled_data)[0]
        # 5. Send result back to UI
        return render_template(
            "home.html",
            prediction=round(float(prediction), 2)
        )
    else:
        return render_template("home.html")
        

if __name__ == "__main__":
    app.run(debug=True)
