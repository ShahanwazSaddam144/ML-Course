from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

# Real scores
real_scores = [90,60,80,100]

# Model Guess
predicted_scores = [85,70,70,95]

mae = mean_absolute_error(real_scores, predicted_scores)
mse = mean_squared_error(real_scores, predicted_scores)

rmse = np.sqrt(mse)

print("MAE: On Average off by:", mae)
print("MSE: On Squared Mistake Value", mse)
print("RMSE: Final Realistic error", rmse)