from sklearn.datasets import load_breast_cancer
dataset = load_breast_cancer()

X = dataset.data
y = dataset.target
#print(len(y))
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,shuffle=True,stratify=y)

#print (len(X_test))
from sklearn.svm import SVC
svc = SVC(kernel="linear")
svc.fit(X_train,y_train)
#print (SVC)

from sklearn.metrics import accuracy_score
y_test_pred = svc.predict(X_train)
#print(y_test)
print(accuracy_score(y_train,y_test_pred))





