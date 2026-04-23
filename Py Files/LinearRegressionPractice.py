from sklearn.linear_model import LinearRegression

X=[[1],[2],[3],[4],[5]]
Y=[40,60,70,80,90]

model = LinearRegression()
model.fit(X,Y)

while True:
 hours = float(input("Enter hours you studied:"))
 predicted_marks = model.predict([[hours]])
 print(f"Based on your studied hours {hours} your predicted marks should be {predicted_marks}")
