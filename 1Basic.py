                            #Supervised Learning
#has a label
from sklearn import tree
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = ['orange', 'orange', 'apple', 'apple']
clf = tree.DecisionTreeClassifier() #make fungsi to call Decision Tree Classifier
clf = clf.fit(features, labels) #fit : find the patern between feature and label

print(clf.predict([[165, 1]]))
print(clf.predict([[145,1]]))

'''
from sklearn import tree
features = [[140, 'smooth'], [130, 'smooth'], [150, 'bumpy'], [170, 'bumpy']]
labels = ['orange', 'orange', 'apple', 'apple']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

print (clf.predict([[145,1]]))
'''
