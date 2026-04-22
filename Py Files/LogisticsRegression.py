from sklearn.linear_model import LogisticRegression

X = [[1],[2],[3],[4],[5]]
y = [0, 0, 1, 1, 1]

model = LogisticRegression()
model.fit(X, y)

hours = float(input("Enter study hours: "))
result = model.predict([[hours]])[0]

if result == 1:
    print(f"Based on your study hours {hours}, you are likely to be Pass")
else:
    print(f"Based on your study hours {hours}, you are likely to be Fail")