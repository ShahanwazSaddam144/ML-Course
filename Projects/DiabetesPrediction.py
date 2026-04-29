import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

dataFrame = pd.read_csv("C:\ML Course\Projects\diabetes.csv")

X = dataFrame.drop("Outcome", axis=1)
Y = dataFrame["Outcome"]

X_Train, X_Test, Y_Train, Y_Test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = LogisticRegression(max_iter=1000)

model.fit(X_Train, Y_Train)

Y_pred = model.predict(X_Test)

# Evaulation
print("Accuracy:", accuracy_score(Y_Test, Y_pred))
print("Precision:", precision_score(Y_Test, Y_pred))
print("Recall:", recall_score(Y_Test, Y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(Y_Test, Y_pred))

sample = [[2, 120, 70, 20, 79, 25.0, 0.5, 30]]

prediction = model.predict(sample)

if prediction[0] == 1:
    print("\nPrediction: Diabetic")
else:
    print("\nPrediction: Not Diabetic")