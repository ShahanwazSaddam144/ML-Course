import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

data = pd.read_csv("C:\ML Course\Projects\student_read.csv")

X = data[['Hours']] # double brackets #2D
Y = data[['Score']]

model = LinearRegression()
model.fit(X,Y)

predicted_score = model.predict(X)

# Evaluate
mae = mean_absolute_error(Y, predicted_score)
mse = mean_squared_error(Y, predicted_score)
rmse = np.sqrt(mse) 

print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("Root Mean Squared Error (RMSE):", rmse)\

predication_input = float(input("Enter hours you studied:"))

new_predication = model.predict([[predication_input]])
print(f"Predicted Score for {predication_input} hours:", new_predication)