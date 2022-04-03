# # sphinx_gallery_thumbnail_number = 3
# import matplotlib.pyplot as plt
# import matplotlib
# import numpy as np

# fig, ax = plt.subplots()  # Create a figure containing a single axes.
# fig
# ax
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
# plt.show()
# matplotlib.get_backend()

# plt.plot([1, 2, 3, 4], [1, 8, 8, 3])  # Matplotlib plot.
# plt.show()
-
import numpy as np
from matplotlib import pyplot as plt
 
x = np.arange(1,11)
y =  2  * x +  5

plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x,y,'ob')
plt.show()

x = np.arange(0,  3  * np.pi,  0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()

x = np.arange(0,  3  * np.pi,  0.1) 
y_sin = np.sin(x) 
y_cos = np.cos(x)  
# 建立 subplot 网格，高为 2，宽为 1  
# 激活第一个 subplot
plt.subplot(2,  1,  1)  
# 绘制第一个图像 
plt.plot(x, y_sin) 
plt.title('Sine')  
# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(2,  1,  2) 
plt.plot(x, y_cos) 
plt.title('Cosine')  
# 展示图像
plt.show()

x =  [6,8,10] 
y =  [12,16,6] 
x2 =  [6,9,11] 
y2 =  [6,15,7] 
plt.bar(x, y, align =  'center') 
plt.bar(x2, y2, color =  'g', align =  'center') 
plt.title('Bar graph') 
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.show()