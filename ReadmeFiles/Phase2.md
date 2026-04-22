## Data ReProcessing (Preparing Data)

## Standard Scalar

Defination:
StandardScaler (from scikit-learn) is a preprocessing tool used to standardize numerical data.

Libaries:
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

Structure:
standard_scalar = StandardScaler()
standard_scaled = standard_scalar.fit_transform(dataFrame)

---

## MinMax Scalar

Defination:
Min-Max Scaler (Normalization) is a technique used in machine learning to rescale
numerical data into a fixed range—usually 0 to 1.

x = original value
x
min
	​

 = smallest value in the dataset
x
max
	​

 = largest value in the dataset
x
′
 = scaled value (between 0 and 1)

 Structure:
 minmax_scalar = MinMaxScaler()
minmax_scaled = minmax_scalar.fit_transform(dataFrame)
----------------------------------------------------

Train-Test Split
--------------------------
Defination:
train_test_split is a function used in machine learning to divide your dataset into two parts:

Training set → used to train the model
Testing set → used to evaluate how well the model performs on unseen data

Code:
from sklearn.model_selection import train_test_split

X = [1, 2, 3, 4, 5]
y = [10, 20, 30, 40, 50]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)