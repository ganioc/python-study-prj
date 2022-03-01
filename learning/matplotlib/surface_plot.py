import numpy as np
from mpl_toolkits.mplot3d import Axes3D  
# Axes3D import has side effects, it enables using projection='3d' in add_subplot
import matplotlib.pyplot as plt
import random

def fun(x, y):
    return x + y

def fun2(x,y):
    return 3*x - y

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(0, 8.0, 0.05)
X, Y = np.meshgrid(x, y)
zs = np.array(fun2(np.ravel(X), np.ravel(Y)))
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

plt.show()

