from sklearn.preprocessing import LabelEncoder 
import pandas as pd

data = pd.read_csv("Py Files/sample_data.csv")

data_label = data.copy()
le = LabelEncoder()

data_label['Gender_Encoded'] = le.fit_transform(data_label['Gender'])
data_label['Passed_Encoded'] = le.fit_transform(data_label['Passed'])

print('\nLabel Encoded Data')
print(data_label[['Name','Gender','Gender_Encoded','Passed','Passed_Encoded']])