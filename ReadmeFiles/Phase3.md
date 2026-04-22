Supervised Machine Learning
-----------------------------

Fit and Predict:
.............................
Fit:
fit() is used to teach the model from data.

Predict:
predict() is used after training to make predictions on new data.
-------------------------------------------------------------

Regression:
Regression is a concept in machine learning and statistics used to predict a 
numerical (continuous) value based on input data.

👉 Example:

Study Hours → Predict Test Score
Experience → Predict Salary

Types of Regression:
Linear Regression → straight line relationship
Multiple Regression → multiple inputs
Polynomial Regression → curved relationship
----------------------------------------------

Linear Regression:
Linear Regression is a method in machine learning and statistics used to 
predict a numerical value by fitting a straight line to the data.

Definition (simple)
Linear regression finds the best straight-line relationship between:

Input (X) → independent variable
Output (y) → dependent variable

Libaries to Import:
from sklearn.linear_model import LinearRegression

Example Code:
from sklearn.linear_model import LinearRegression

X = [[1],[2],[3],[4],[5]]
Y = [40,50,65,75,90]

model = LinearRegression()
model.fit(X,Y)

hours = float(input("Enter how many hours you study:"))

predicted_marks = model.predict([[hours]])
print(f"Based on your hours {hours} you studied your predicted marks is {predicted_marks}")
----------------------------------------------------------------------------------


Logistics Regression:
Logistic regression is used when the output is not a number, but a class or category.

👉 Examples:

Pass / Fail
Spam / Not Spam
Disease / No Disease

Libaries:
from sklearn.linear_model import LogisticRegression

Example Code:
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
------------------------------------------------------------------

K-Nearest Neighbors (KNN) Classifier:
KNN classifies a new data point by looking at the ‘K’ nearest
neighbors and choosing the majority class among them.

How it works:
Choose a value of K (e.g., 3 or 5)
Find the K closest data points to the new input
Check their labels (Pass/Fail, Yes/No, etc.)
Assign the most common label

Libaries:
from sklearn.neighbors import KNeighborsClassifier

Example Code: 
from sklearn.neighbors import KNeighborsClassifier

X = [
    [100,7],
    [200,7.5],
    [250,8],
    [300,9.5],
    [330,9],
    [360,9.5]
]

Y = [0,0,0,1,1,1] #Note that 0 = Apple and 1 = Orang

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X,Y)

weight = float(input("Enter the weigh in grams:"))
size = float(input("Enter the size in cm:"))

predication = model.predict([[weight, size]])

if predication == 0:
    print("It's likely to be Apple")

else:
    print("It's is likely to be orange")