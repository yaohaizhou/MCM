import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
# ax = Axes3D(fig)
ax = plt.axes(projection="3d")

ax.set_xlabel("x axis")
ax.set_ylabel("y axis")
ax.set_title('3d plot')
ax.set_zlabel('z axis')

xx = np.linspace(-5, 5, 100)
yy = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(xx, yy)
Z = np.sin(X) + np.cos(Y)
ax.plot_surface(X, Y, Z, cmap='rainbow', rstride=1, cstride=1)
ax.contour(X, Y, Z, offset=-2, cmap="rainbow")
plt.show()
