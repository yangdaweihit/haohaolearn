# 导入截面

在桥梁的杆系模型中需要定义很多截面，在ANSYS中定义这些截面是非常低效的。
一种实用的方式是在AutoCAD中绘制这些截面并输出为`.sat`文件，由ANSYS的连接
命令`~SATIN`引入为面，然后划分单元生成截面。

示例代码参见[importsat.ans](importsat/importsat.ans)