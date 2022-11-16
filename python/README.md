# Python


## 背景

- [Python简史](https://www.cnblogs.com/vamei/archive/2013/02/06/2892628.html)

## 官方文档

关于Python的所有信息都源自官方文档。所谓文档，是一个包括入门教程、库手册、
语法手册、安装和用法等在内的文本集合。几乎不太可能在阅读过所有文档后再使
用Python。一方面内容太多，另一方面文档也会随着版本升级而有所变化。文档的
意义在于，它对Python提供了最具权威的解释，供我们探究本源。

- [官方文档](https://docs.python.org/3/index.html)
- [官方教程(中文)](https://docs.python.org/zh-cn/3/tutorial/)
- [标准库(中文)](https://docs.python.org/zh-cn/3/library/index.html#library-index) 
- [术语(中文)](https://docs.python.org/zh-cn/3/glossary.html#glossary)

## 教程 

- [Python-100天从新手到大
  师](https://github.com/jackfrued/Python-100-Days)：自学最佳路径
- [python3菜鸟教程](http://www.runoob.com/python3/python3-tutorial.html)
- [python-course](https://www.python-course.eu/index.php)
  - [Numerical Programming with Python](https://www.python-course.eu/numerical_programming_with_python.php)
- [realpytho](https://realpython.com): real python团队
- [BogoToBogo](https://www.bogotobogo.com/python/pytut.php): BogoToBogo
- [matplotlib tutorials](https://matplotlib.org/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py)
- [正则表达式30分钟入门课程](https://deerchao.cn/tutorials/regex/regex.htm)
  
## pip

- pip是Python的包管理器，使用pip可以从[Python Package Index(PyPI)](pypi.org)中下载包。
- [pip笔记](./doc/pip.md)

## 笔记 

### 环境和工具

- [overview](./doc/overview.md)：综述
- [pycharm](./doc/pycharm.org): IDE
- [elpy](./doc/elpy.md): Emacs中Python的编辑环境
- [jupyter](./doc/jupyter.org): 优秀的交互环境
- [debug](./doc/debug.org): Linux下的调试工具
- [virtualenv](./doc/virtualenv.org): 虚拟环境
- [site-packages](./doc/site-packages.md): 自定义库

### 语法

- [numpy](./doc/numpy.md)
- [string](./doc/string.org): 字符串
- [regex](./doc/regex.org): 正则表达式 
- [pandas](./doc/pandas.md): 数据处理
- [argparse](./doc/argparse.org): 参数解析
- [os.path](./doc/os-path.org): 目录和文件
- [sympy](./doc/sympy.org): 解方程
- [数值编程](./doc/numericalprogram.md)

### 实践

- [p001-numpy](./practice/p001-numpy.py)
- [p002-numpy](./practice/p002-numpy.py)
- [p003-string](./practice/p003-string.py)
- [p004-argparse](./practice/p004-argparse.py)
- [p004-set](./practice/p005-set.py): 见[set](https://www.programiz.com/python-programming/set)介绍
- [p006-map](./practice/p006-map.py): 见[map](https://www.geeksforgeeks.org/python-map-function/)函数介绍
- [p007-sympy](./practice/p007-sympy.py)
- [p008-scipy](./practice/p008-scipy.py)
- [p009-numpy-io](./practice/p009-numpy-io.py)
- [p010-scipy-interpolation](./practice/p010-scipy-interpolation.py)
- [p011-os](./practice/p011-os.py)
- [p012-builtin-function](./practice/p012-builtin-function.py)
- [p013-stdtypes](./practice/p013-stdtypes.py)
- [p014-json](./practice/p014-json.py)
- [p015-json](./practice/p015-nestlist.py)
- [p016-pandas](./practice/p016-pandas.py)
    

## 配置

- Linux
  - 安装pip3: sudo apt install python3-pip
  - 配置 `.pip/pip.conf`
    ```
	[global]
	index-url = https://mirrors.aliyun.com/pypi/simple/

	[install]
	trusted-host=mirrors.aliyun.com

    ```
  - 升级pip3: python3 -m pip install --upgrade pip
  - 安装包：pip3 install numpy pandas
  - 安装vitualenv: pip3 install virtualenv
  - 配置路径: export PATH="$PATH:~/.local/bin"
