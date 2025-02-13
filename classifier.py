import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import pickle

def performTraining():
    df = pd.read_csv("./data/Iris.csv")
    X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
    Y = df['Species']

    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.30, shuffle=True)
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)  # training the classifier on Training data
    y_pred = clf.predict(X_test)  # testing the classifier on testing dataset

    print(f"the accuracy of the model is {accuracy_score(y_test, y_pred) * 100}%")

    #with open("./model/iris_classifier.pkl", "wb") as f:
    with open("./model/iris_classifier.pkl", "wb") as f:
        pickle.dump(clf, f)