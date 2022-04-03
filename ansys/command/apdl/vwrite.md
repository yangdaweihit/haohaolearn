# *VWRITE 

用`*VWRITE`将数据格式化写入文件。

## 语法
```
*VWRITE, Par1, Par2, Par3, Par4, Par5, Par6, Par7, Par8, Par9, Par10, Par11, Par12, Par13, Par14, Par15, Par16, Par17, Par18, Par19
```

语法年似简单，但命令要义颇多。

## 前提

首先要打开文件准备写入，有2种方式：

- `*CFOPEN, fname, ext, -, Loc` 

打开特定文件用`*vwrite`和`cfwrite`写入。

- `/output, fname, ext, -, Loc`

默认`*vwrite`写入标准输出中——jobname.out或命令窗口。虽然可以用
`/output`重定向到文件中，替代`*.out`或屏幕，但不推荐这种方式。因为其它内
容可能也会写入文件中。

## 参数

`*vwrite`需要在后面跟上格式化定义才能工作。`*vwrite`的参数共有19个，可以
是向量、标量，或字符参数，亦可为常数。

```
    adiv = ' | '
    *dim,nds, ,10
    *dim,temps,,10
    *vfill,nds(1),ramp,1,1
    *vfill,temps(1),rand,70,1500
    *cfopen,vw1.out
    *VWRITE,'Temp: ',nds(1),temps(1),adiv, 'TREF: ',70
    (A6,F8.0,g16.8,A3,A6,F10.4)
    *cfclose
```


## 向量参数

首先要注意：没有`*do`循环。若提供了一个向量参数，`*vwrite`会从给定参数循
环到向量尾。如果并不希望写出全部向量，可将`*VLEN`和`*VMASK`写在｀
*VWRITE`命令之前：

- `*VLEN, nrow, ninc`

只写出`nrow`个元素，并按`ninc`跳过；
```
% 只输出A()的第4个元素
*VLEN,1
*VWRITE,A(4)
(G16.8)
```

- `*VMASK, Par`

可以定义一个由0和1构成，长度与输出向量一样的蒙板向量，由`*VMASK`提供。｀
*vwrite`将只输出蒙板向量中非零值对应的指标处的值。

输出向量可以多维的。`*VWRITE`只对第1个指标循环。若有一个向量xyz存储了X，
Y, Z坐标，输出形式如下：
```
*VWRITE, xyz(1,1), xyz(1,2), xyz(1,3)
(3G16.8)
```

## 整数

按FORTRAN格式无法输出整数，当需要输出整数时，可按C格式输出：`%I`。


## 关闭文件

在完成输出后，需要用`*CFCLOSE`关闭文件。

## 其它

- 不能在命令行中用粘贴或键入的方式使用`*VWRITE`，只能通过从文件读取的方
  式。

- 在`*VWRITE`后不能是空白行，否则会在这一行停止运行。若需要输出空白行，
  可以用`''`或X FORTRAN描述符说明。

- 还要了解`*CFWRITE`，当需要用宏写出宏时，最好用这个命令，它不需要格式修
  饰符。
  
- 若各向量参数不等长，会按最长的向量循环，其它较短向量将会被补零，对于字
  符数组，会补入空白符。
  
## 格式化语句

使用`*VWRITE`最关键亦是最难的部分就是格式化语句。在输出大量列式数据时，
推荐使用FORTRAN格式化语句。若用于报告输出，涉及丰富信息文本、或向用户发
出消息时，采用C格式化语句。

今天很多用户已经不了解FORTRAN语句，请参见[Format
statements](https://web.stanford.edu/class/me200c/tutorial_77/17_format.html)

基本格式为：( [n]格式代码[w[.d]])

| 格式代码 | 描述     |
| ---      | ----     |
| A        | 字符串   |
| D	    | 双精度   |
| E	    | 指数     |
| F	    | 固定浮点 |
| X	    | 空格     |
| /	    | 新行     |

- F,D,E后面有通用形式`w.d`，w表示域宽，d表示小数点后有效数字; 
- 对于X，可以前面加入`n`，表示n个空格。


## 参考

- [Writing Text files with *VWRITE](http://www.padtinc.com/blog/writing-text-files-with-vwrite/)
- *VWRITE, Mechanical APDL Command Reference 
