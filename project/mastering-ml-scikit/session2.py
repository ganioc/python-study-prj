# coding: utf-8
import numpy as np
X = np.array([[6],[8], [10], [14], [18]]).reshape(-1,1)
x_bar = X.mean()
print(x_bar)
variance = ((X - x_bar)**2).sum()/(X.shape[0] -1)
print(variance)
print(np.var(X, ddof=1)







)
