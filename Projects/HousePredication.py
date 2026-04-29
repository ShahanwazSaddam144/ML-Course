import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = {
    "area": [1000, 1500, 2000, 2500, 3000],
    "bedrooms": [2, 3, 3, 4, 5],
    "location": ["A", "B", "A", "B", "C"],
    "price": [200000, 300000, 400000, 500000, 650000]
}

df = pd.DataFrame(data)

location_map = {
    "A": 1,
    "B": 2,
    "C": 3
}

df["location"] = df["location"].map(location_map)

X = df[["area", "bedrooms", "location"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "house_price_model.pkl")

print("Model trained & saved!")

area = int(input("Enter area: "))
bedrooms = int(input("Enter bedrooms: "))
location = input("Enter location (A/B/C): ")

location_encoded = location_map[location]

input_data = [[area, bedrooms, location_encoded]]

prediction = model.predict(input_data)

print("Predicted Price:", prediction[0])