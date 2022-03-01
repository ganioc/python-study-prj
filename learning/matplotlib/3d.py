from mpl_toolkits import mplot3d 

import numpy as np
import matplotlib.pyplot as plt 

print("mplot3d begin ...")

fig = plt.figure()
ax = plt.axes(projection='3d')

# Data for a three-dimensional line
xline = np.linspace(0, 8, 100)
yline = np.linspace(0,8,100)
zline = np.add(xline,yline)
ax.plot3D(xline, yline, zline, 'gray')
plt.show()

