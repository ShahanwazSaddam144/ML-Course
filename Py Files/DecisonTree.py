from sklearn.tree import DecisionTreeClassifier

X = [
    [7,2],
    [8,3],
    [9,8],
    [10,9]
]

Y = [0,0,1,1] #Note that 0 = Apple and 1 = Orange

model = DecisionTreeClassifier()
model.fit(X,Y)

size = float(input("Enter size in cm:"))
shade = float(input("Enter shade between (1-10):"))

result = model.predict([[size, shade]])

if result == 0:
    print("It's is likely to be Apple")
else:
    print("It's likely to be Orange")