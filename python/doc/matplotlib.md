# Matplotlib

## 什么是pyplot
- pyplot是matplotlib中的一个模块。 
- matplotlib.pyplot: 基于状态的交互界面。

## 两种画图接口

- MATLAB风格接口: matplotlib.pyplot.plot()函数。设定图形风格是通过pyplot
  的函数实现的。由于这种接口是基于状态的：它会持续跟踪当前的图形和坐标轴。
  不容易回到之前的图形上设置属性。所以这种只适合生成并设置一个图的情境。
  方式是调用pyplot的函数，见[pyplot api](https://matplotlib.org/api/index.html)

- 面向对象接口：fig, ax = matplotlib.pyplot.subplots()生成Figure和Axes对
  象。可通过Axes对象的索引设置各个子图。方式是调用不同Axes对象的函数。这
  些函数见：[axes api](https://matplotlib.org/api/axes_api.html)


## 什么是figure和axes
- matplotlib.pyplot.figure(): 生成一个图形。figure是一个能容纳坐标轴、图
  形、文字和标签的容器。
- matplotlib.pyplot.axes(): 在当前图上增加一个axes(一块画图区域，包括：
  axis, tick, line2d, text, polygen等)，并设置为当前axes。axes是一个矩形
  区域。
- 一个figure是一个图形实例，一个axes表示一个坐标轴实例或一组坐标轴实例。
- 生成figure和axes有两种方式：
  + fig, ax = plt.subplots(...) # 生成一个图形和一组子图
  + 注意，还有一个subplot函数，是在当前图形上增加一个子图
  + fig = plt.figure(); ax = plt.axes(); 
  
