from sklearn import svm
from sklearn import datasets, metrics

iris = datasets.load_iris()

classifier = svm.SVC()

classifier.fit(iris.data, iris.target)
pred = classifier.predict(iris.data)
score = metrics.accuracy_score(iris.target, pred)

print "Accuracy  %f  " % score
