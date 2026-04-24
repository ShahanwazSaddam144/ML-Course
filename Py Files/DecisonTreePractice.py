from sklearn.tree import DecisionTreeClassifier

X = [
    [7,2],
    [8,3],
    [9,8],
    [10,9],
    [11,10]
]

Y = [0,0, 1,1,0]

model = DecisionTreeClassifier()
model.fit(X, Y)

while True:

 size = float(input("Enter size in cm:"))
 shade = float(input("Enter shade in (1-10):"))

 result = model.predict([[size, shade]])

 if result == 0:
    print("It is likely to be Apple")
 else:
    print("It is likely to be orange")