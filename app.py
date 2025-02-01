from flask import Flask, request, jsonify
from sklearn.tree import DecisionTreeClassifier
import pickle
import numpy as np
import classifier

# initialize the flask app
app = Flask(__name__)

@app.route("/prediction", methods=["POST"])
def prediction():
    with open("./model/iris_classifier.pkl", "rb") as f:
        clf = pickle.load(f)
    payload = request.json
    x_unknown = [payload["sepal-lenght"],payload["sepal-width"],payload["petal-lenght"],payload["petal-width"]]
    x_unknown = np.array(x_unknown).reshape(1,-1)
    prediction = clf.predict(x_unknown)
    print(payload)
    return jsonify({"predicted_value":prediction[0]})

@app.route("/hello", methods=["GET"])
def foo():
    return "<h3> Welcome to MLOps Class"

@app.route("/training", methods=["GET"])
def trainNew():
    classifier.performTraining()
    return "<h3> Classifier Trained Successfully"

if __name__ == "__main__":
    app.run(port=5003)