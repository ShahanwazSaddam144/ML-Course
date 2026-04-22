from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4],[5]]
Y = [40,50,65,75,90]

model = LinearRegression()
model.fit(X,Y)

hours = float(input("Enter how many hours you study:"))

predicted_marks = model.predict([[hours]])
print(f"Based on your hours {hours} you studied your predicted marks is {predicted_marks}")