import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import time


def pure_python_version():
    t1 = time.time()
    X = range(size_of_vec)
    Y = range(size_of_vec)
    Z = [X[i] + Y[i] for i in range(len(X))]
    return time.time() - t1


def numpy_version():
    t1 = time.time()
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)
    Z = X + Y
    return time.time() - t1


# https://www.python-course.eu/numpy.php
# 用列表初始化一维数组
cvalues = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]
C = np.array(cvalues)
print(C)
type(C)  # ndarray类型就是一般所说的array

fvalues = [x * 9 / 5 + 32 for x in cvalues]
print(fvalues)

plt.plot(C)
plt.show()  # 没打印出来

size_of_vec = 1000
t1 = pure_python_version()
t2 = numpy_version()
print(t1, t2)
print("Numpy is in this example " + str(t1 / t2) + " faster!")

np.arange(1.2, 3.4, 0.1)
x = np.arange(10.4)
print(x)
x = np.arange(0.5, 10.4, 0.8, int)
print(x)

print(np.linspace(1, 10, 8))
print(np.linspace(1, 10, 7, False))
print(np.linspace(1, 10, 8, False))
print(np.linspace(1, 10, 8, True))
samples, spacing = np.linspace(1, 10, retstep=True)
print(spacing)
print(samples)

dt = np.dtype([('density', np.int32)])
dx = np.array([(393, ), (337, ), (256, )], dtype=dt)
print(dx)
dt = np.dtype('<d')
print(dt.name, dt.byteorder, dt.itemsize)

df = pd.DataFrame({'a':np.arange(10)})
new_df = pd.DataFrame(np.arange(22).reshape(11,2), columns=['a', 'b'])
df = pd.concat([df,new_df],axis=1)
