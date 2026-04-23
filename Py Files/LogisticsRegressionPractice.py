from sklearn.linear_model import LogisticRegression

X=[[1],[2],[3],[4],[5]]
Y=[0,0,1,1,1] # Notice 1=skilled 0 = non-skilled

model = LogisticRegression()
model.fit(X,Y)

while True:
 coding_hours = int(input("Enter your coding practice hours:"))
 coding_skill = model.predict([[coding_hours]])[0]

 if coding_skill == 1:
  print(f"Based on your coding pratice hours {coding_hours} ,you are a skill programmer")
 else:
  print(f"Based on your coding pratice hours {coding_hours}, you are a non-skill programmer")