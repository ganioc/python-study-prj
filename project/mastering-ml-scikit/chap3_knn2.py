import numpy as np

from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

X_train = np.array([
    [158,1],
    [170,1],
    [183,1],
    [191,1],
    [155,0],
    [163,0],
    [180,0],
    [158,0],
    [170,0]
])
y_train = [64, 86, 84, 80, 49, 59, 67, 54, 67]

X_test = np.array([
    [168,1],
    [180,1],
    [160,0],
    [169,0]
])
y_test = [65, 96, 52, 67]

K=3
clf = KNeighborsRegressor(n_neighbors=K)
clf.fit(X_train, y_train)

predictions = clf.predict(X_test)
print('Predicted weights: %s' % predictions)
print('Coefficient of determination: %s' % r2_score(y_test,
    predictions))
print('Mean absolute error: %s' % mean_absolute_error(y_test,
    predictions))
print('Mean squared error: %s' % mean_squared_error(y_test,
    predictions))


##
from scipy.spatial.distance import euclidean

X_train = np.array([
    [1700,1],
    [1600,0]
    ])
x_test = np.array([1640,1]).reshape(1, -1)
print(euclidean(X_train[0,:], x_test))
print(euclidean(X_train[1,:], x_test))

X_train = np.array([
    [1.7,1],
    [1.6, 0]
])
x_test = np.array([164,1]).reshape(1,-1)
print(euclidean(X_train[0,:], x_test))
print(euclidean(X_train[1,:], x_test))

##
from sklearn.preprocessing import StandardScaler

ss = StandardScaler()
X_train_scaled = ss.fit_transform(X_train)

print(X_train)
print(X_train_scaled)




















