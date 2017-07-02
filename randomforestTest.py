from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
import numpy as np
from sklearn.cross_validation import cross_val_score, ShuffleSplit
from treeinterpreter import treeinterpreter as ti

from sklearn.datasets import load_iris
from sklearn.datasets import load_svmlight_file

inputFile = open('iris.txt','r')
lines = inputFile.readlines()

label_list = []
label_dict = {}
record_label = ""
label_id = -1
x_train = []
for line in lines:
    line = line.strip().split(",")
    label_tmp = line[len(line)-1]
    if not label_tmp==record_label:
        label_id += 1
        record_label = label_tmp
        label_dict[label_id] = record_label
    label_list.append(label_id)
    list = []
    for i in range(0,len(line)-1):
        list.append(line[i])
    x_train.append(np.array(list,dtype=float))
y_train = label_list

# x_train,y_train = load_svmlight_file("iris.txt")

rf = RandomForestRegressor()
rf.fit(x_train, y_train)

instance = []
instance.append(x_train[50])
instance.append(x_train[102])
instance = np.array(instance)

print 'instance 0 prediction:',rf.predict(instance[0]),label_dict[(int)(rf.predict(instance[0])[0])]
print 'instance 1 prediction:',rf.predict(instance[1]),label_dict[(int)(rf.predict(instance[1])[0])]
print y_train[50],y_train[102]


feature_list = ['petal length (cm)','petal width (cm) -0.03','sepal length (cm)','sepal width (cm)']
prediction, bias, contributions = ti.predict(rf, instance)#Printint out the results:for i in range(len(instances)):    print "Instance", i    print "Bias (trainset mean)", bias[i]    print "Feature contributions:"
for i in range(len(instance)):
    print "Instance", i
    print "Bias (trainset mean)", bias[i]
    print "Feature contributions:"
    for c, feature in sorted(zip(contributions[i],
                                 feature_list),
                             key=lambda x: -abs(x[0])):
        print feature, round(c, 2)
    print "-"*20


print '================================================'
print 'Following analysis is based on original datasets:'
print '================================================'
# show contribution of each feature
iris=load_iris()
X = iris["data"]
Y = iris["target"]
names = iris["feature_names"]
rf = RandomForestRegressor()
scores = []
for i in range(X.shape[1]):
     score = cross_val_score(rf, X[:, i:i+1], Y, scoring="r2",
                              cv=ShuffleSplit(len(X), 3, .3))
     scores.append((round(np.mean(score), 3), names[i]))
print sorted(scores, reverse=True)

rf_new=RandomForestRegressor()
rf_new.fit(iris.data[:150],iris.target[:150])

instances=iris.data[[88,109]]
print 'instance 0 prediction:',rf_new.predict(instances[0])
print 'instance 1 prediction:',rf_new.predict(instances[1])
print iris.target[88],iris.target[109]

prediction, bias, contributions = ti.predict(rf_new, instances)#Printint out the results:for i in range(len(instances)):    print "Instance", i    print "Bias (trainset mean)", bias[i]    print "Feature contributions:"
for i in range(len(instances)):
    print "Instance", i
    print "Bias (trainset mean)", bias[i]
    print "Feature contributions:"
    for c, feature in sorted(zip(contributions[i],
                                 iris.feature_names),
                             key=lambda x: -abs(x[0])):
        print feature, round(c, 2)
    print "-"*20
