import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata



# 一维插值
"""
x = np.linspace(-5,5,9)
y = np.cos(x**3+x+5)

kinds = ["linear","nearest","zero","slinear","quadratic","cubic","previous","next"]
x_new = np.linspace(-5,5,500)
plt.subplot(3,1,1)
plt.scatter(x,y,label="Original data")
for kind in kinds[0:3]:
    f = interpolate.interp1d(x,y,kind=kind)
    y_new = f(x_new)
    plt.plot(x_new,y_new,label=kind)
plt.legend(loc = (1,0.7))
plt.subplot(3,1,2)
plt.scatter(x,y,label="Original data")
for kind in kinds[3:-2]:
    f = interpolate.interp1d(x,y,kind=kind)
    y_new = f(x_new)
    plt.plot(x_new,y_new,label=kind)
plt.legend(loc = (1,0.7))
plt.subplot(3,1,3)
plt.scatter(x,y,label="Original data")
for kind in kinds[-2:]:
    f = interpolate.interp1d(x, y, kind=kind)
    y_new = f(x_new)
    plt.plot(x_new,y_new,label=kind)
plt.legend(loc = (1,0.7))
plt.show()
"""
# 二维插值
def func(x, y):
    return x*(1-x)*np.cos(4*np.pi*x) * np.sin(4*np.pi*y**2)**2

grid_x, grid_y = np.meshgrid(np.linspace(-5,5,10),np.linspace(-5,5,10))
points = np.random.rand(1000, 2)
values = func(points[:,0], points[:,1])
grid_z0 = griddata(points, values, (grid_x, grid_y), method='nearest')
grid_z1 = griddata(points, values, (grid_x, grid_y), method='linear')
grid_z2 = griddata(points, values, (grid_x, grid_y), method='cubic')

plt.subplot(221)
plt.imshow(func(grid_x, grid_y).T, extent=(0,1,0,1), origin='lower')
plt.plot(points[:,0], points[:,1], 'k.', ms=1)
plt.title('Original')
plt.subplot(222)
plt.imshow(grid_z0.T, extent=(0,1,0,1), origin='lower')
plt.title('Nearest')
plt.subplot(223)
plt.imshow(grid_z1.T, extent=(0,1,0,1), origin='lower')
plt.title('Linear')
plt.subplot(224)
plt.imshow(grid_z2.T, extent=(0,1,0,1), origin='lower')
plt.title('Cubic')
plt.gcf().set_size_inches(6, 6)
plt.show()
