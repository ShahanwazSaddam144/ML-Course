from sklearn.neighbors import KNeighborsClassifier

X = [
    [100,7],
    [170,7.5],
    [200,8],
    [250,8.5],
    [300,9],
    [350,9.5]
]

Y = [0,0,0,1,1,1] #Note that 0 = Apple and 1 = Orange

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,Y)


while True:

  weight = float(input("Enter your weights in grams:"))
  size = float(input("Enter your size in cm:"))

  predication = model.predict([[weight, size]])[0]

  if predication == 0:
    print("Apple")

  else:
    print("Orange")