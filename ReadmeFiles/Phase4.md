Mastering Model Evaluations
-----------------------------

📊 What are sklearn Metrics?

Metrics measure the performance of a model by comparing:

Actual values (true labels)
Predicted values (model output)
---------------------------------------------------------

📊 What are Regression Metrics?

They compare:

Actual value (y_true)
Predicted value (y_pred)

and calculate the error between them.
-------------------------------------------

📊 What is a Confusion Matrix?

A Confusion Matrix is a table that shows how well your model is performing by comparing:

Actual values
Predicted values
--------------------------------------------------

📊 What are Classification Metrics?

They compare:

Actual labels (y_true)
Predicted labels (y_pred)

and measure how correct your predictions are.
-------------------------------------------------

Matics Code:
--------------------------
Mean Absolute Error (MAE):
MAE is a regression evaluation metric used to measure how far predictions are from actual values.

Key Points
MAE calculates the average of absolute errors
It does not square errors (unlike MSE)
Easy to understand because it’s in the same units as data
Less sensitive to outliers compared to squared-error metrics.
---------------------------------------------------------------

Mean Squared Error (MSE):
MSE is a common regression evaluation metric in machine learning. It measures the average 
of the squared differences between actual and predicted values.

Key Points
Measures how close predictions are to actual values
Sensitive to outliers (large errors increase MSE a lot)
Always non-negative (0 = perfect prediction).
-----------------------------------------------------------

Root Mean Squared Error (RMSE):
RMSE is a regression evaluation metric that measures how far predicted values are 
from actual values. It is simply the square root of MSE.

Key Points
RMSE is in the same units as the original data (unlike MSE)
Penalizes large errors more (because of squaring)
Lower RMSE means better model performance
Always ≥ 0 (0 = perfect predictions)
---------------------------------------------------

