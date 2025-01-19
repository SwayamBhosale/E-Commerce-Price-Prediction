from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        try:
            rating = float(request.form["rating"])
            prediction = model.predict(np.array([[rating]]))[0]
            prediction = round(prediction, 2)
        except Exception as e:
            prediction = f"Error: {e}"
    return render_template("index.html", prediction=prediction)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        rating = float(request.form["rating"])
        prediction = model.predict(np.array([[rating]]))[0]
        prediction = round(prediction, 2)
        return render_template("index.html", prediction=prediction)
    except Exception as e:
        return render_template("index.html", prediction=f"Error: {e}")

if __name__ == "__main__":
    app.run(debug=True)