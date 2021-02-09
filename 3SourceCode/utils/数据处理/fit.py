# 曲线拟合问题
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# 非线性最小二乘法
def fun(x:np.ndarray,A,B,C,D):
    return A*np.cos(x*B) + x*C +D

x = np.linspace(-5,5,50)
y = fun(x,5,2,5.65,2) + 0.5*np.random.randn(50)
A,B,C,D = curve_fit(fun,x,y)[0]
plt.scatter(x,y,marker='o',label='points',c='orange')
x_new = np.linspace(-5,5,500)
y_new = fun(x_new,A,B,C,D)
plt.plot(x_new,y_new,label="curve_fitting")
plt.legend()
print("A:",A,"B",B,"C",C,"D",D)
plt.show()
