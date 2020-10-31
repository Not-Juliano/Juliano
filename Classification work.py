import pandas as pd
# Import scikit learn
import sklearn
from sklearn import svm
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC


# reading data in from Iris. 'data' is now the iris data.
data = pd.read_csv(r'C:\Users\Me\Desktop\csv\iris.csv')

# checking data
print(data.head(5))

# drop the "ID" column
data.drop('Id', axis=1, inplace=True)

# check
# print(data.head(5))


# Need to define the features and labels


X = data.iloc[:, :-1].values
# The above is a shortned version of this 'X = data.iloc['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm']'


# Now let's tell the dataframe which column we want for the target/labels.
Y = data['Species']


X_train, X_test, y_train, y_test = train_test_split(
    X, Y, test_size=0.20, random_state=20)

print(X_train, y_train)


SVC_model = svm.SVC()
# KNN model requires you to specify n_neighbors,
# the number of points the classifier will look at to determine what class a new point belongs to
KNN_model = KNeighborsClassifier(n_neighbors=5)


# fits
SVC_model.fit(X_train, y_train)
KNN_model.fit(X_train, y_train)

# predictions
SVC_prediction = SVC_model.predict(X_test)
KNN_prediction = KNN_model.predict(X_test)


# Accuracy score is the simplest way to evaluate
print(accuracy_score(SVC_prediction, y_test))
print(accuracy_score(KNN_prediction, y_test))
# But Confusion Matrix and Classification Report give more details about performance
# A confusion matrix is a table or chart, representing the accuracy of a model with regards to two or more classes.
print(confusion_matrix(SVC_prediction, y_test))
print(classification_report(KNN_prediction, y_test))
