import numpy as np

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X_train = np.array([[6],[8],[10], [14], [18]]).reshape(-1, 1)

Y_train = [ 7,9,13,17.5, 18]

X_test = np.array([8,9,11,16,12]).reshape(-1,1)
Y_test = [11,8.5, 15,18,11]

model = LinearRegression()
model.fit(X_train, Y_train)
r_squared = model.score(X_test, Y_test)
print(r_squared)


