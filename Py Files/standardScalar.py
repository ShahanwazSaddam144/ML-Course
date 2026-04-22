import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

data = {
    'StudyHours': [1,2,3,4,5],
    'TestScore': [40,50,60,70,80]
}

dataFrame = pd.DataFrame(data)

standard_scalar = StandardScaler()
standard_scaled = standard_scalar.fit_transform(dataFrame)

print("Standard Scalar Output:")
print(pd.DataFrame(standard_scaled, columns=['StudyHours', 'TestScore']))

minmax_scalar = MinMaxScaler()
minmax_scaled = minmax_scalar.fit_transform(dataFrame)

print("MinMax Scalar Output:")
print(pd.DataFrame(minmax_scaled, columns=['StudyHours', 'TestScore']))

X = dataFrame[['StudyHours']]
Y = dataFrame['TestScore']

X_Train, X_Test, Y_Train, Y_Test = train_test_split(X,Y, test_size=0.2, random_state=2)
print("Training Data")
print(X_Train)

print("Test Data")
print(X_Test)

print("Training Data")
print(Y_Train)

print("Test Data")
print(Y_Test)