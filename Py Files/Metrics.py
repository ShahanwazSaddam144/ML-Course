from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

Y_true = [1,1,1,0,1,1,1]
Y_pred=[1,1,0,0,1,0,1]

print("Accuracy:", accuracy_score(Y_true, Y_pred))
print("Precision:", precision_score(Y_true, Y_pred))
print("Recall:", recall_score(Y_true, Y_pred))
print("F1 Score:", f1_score(Y_true, Y_pred))
