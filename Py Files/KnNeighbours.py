from sklearn.neighbors import KNeighborsClassifier

X = [
    [100,7],
    [200,7.5],
    [250,8],
    [300,9.5],
    [330,9],
    [360,9.5]
]

Y = [0,0,0,1,1,1] #Note that 0 = Apple and 1 = Orange

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,Y)

weight = float(input("Enter the weigh in grams:"))
size = float(input("Enter the size in cm:"))

predication = model.predict([[weight, size]])[0]

if predication == 0:
    print("It's likely to be Apple")

else:
    print("It's is likely to be orange")