import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

data = {
    'StudyHours': [1,2,3,4,5],
    'TestScore': [40,60,80,100,120]
}

dataFrame = pd.DataFrame(data)

# Standard Scaling
standard_scalar = StandardScaler()
standard_scaled = standard_scalar.fit_transform(dataFrame)

print("Standard Scaler Output:")
print(pd.DataFrame(standard_scaled, columns=['StudyHours', 'TestScore']))

# MinMax Scaling
minmax_scalar = MinMaxScaler()
minmax_scaled = minmax_scalar.fit_transform(dataFrame)

print("MinMax Scaler Output:")
print(pd.DataFrame(minmax_scaled, columns=['StudyHours', 'TestScore']))

# Splitting
X = dataFrame[['StudyHours']]
Y = dataFrame[['TestScore']]

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X, Y, test_size=0.4, random_state=4)

print("Training Features:")
print(X_Train)

print("Testing Features:")
print(X_Test)

print("Training Target:")
print(Y_Train)

print("Testing Target:")
print(Y_Test)