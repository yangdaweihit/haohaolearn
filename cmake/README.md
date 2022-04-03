# CMake

学习cmake的第一个材料来自于<https://github.com/TheErk/CMake-tutorial>，编译该项目得`CMake-tutorial.pdf`。

# 介绍

CMake是一个跨平台的编译系统生成器，使其广阔平台上以一种统一方式编译软件变得更为容易。CMake之外还有一些辅助软件可单独或一同使用：

- CMake : 编译系统生成器
- CPack : 包生成器
- CTest :  系统检测驱动器
- CDash : dashboard收集器

# CMake概述一：

## 1. 基本用途

### 编译系统生成品

- CMake是一个生成器：生成原始编译系统文件(Makefile, Ninja, IDE工程文件...)
- CMake脚本语言（声明式）用来描述编译
- 开发者编译`CMakeLists.txt`，调用CMake但不要编辑生成的文件
- CMake可以自动被编译系统再次调用
- CMake流程
- CMake时：运行CMake处理`CMakeLists.txt`
- 编译时：编译工具运行，调用编译器
- 安装时：安装编译出来的库
- CPack时：CPack运行，建立软件包
- 软件包安装时：软件包被安装
  > CMake是一个生成器，即它并不编译源文件，编译源文件的是背后的编译工具(make, XCode, Code::Blocks...)

见第17页，工作流程蓝图。注意：软件包有两种，即`源码包`和`二进制包`。

### 编译一个可执行程序

见第18页，CMake是声明式的脚本语言。它的命令在CMake中编辑在档案中，如： `cmake --help-command add_executable`即列出该命令的说明。

第20页显示了使用CMake编译的方法，非常简单：

- 在源程序目录编写一个`CMakeLists.txt`文件
- 在源程序目录中建立一个build文件夹
- 进入该文件夹，执行`cmake ../上一级文件夹名`
- `make`
- 注意：将生成文件与源码分开，即放在build文件夹中

### 编译程序+匿名库

> 条件编译 我们想保留一个版本，不使用新的Acrodict库，并生成一个新的版本，使用这个库。

假设在源树中有如下文件：

- acrolibre.c 主程序
- acrodict.h 库头文件
- acrodict.c 库源文件
- CMakeLists.txt 将被更新的CMake条目文件

见第23页，在源码中含有一个宏`USE_ACRODICT`，用以判断断编译哪一个部分。

### 编译库i

第25页，CMakeLists.txt文件中第8行，设置目标属性，定义了一个宏`USE_ACRODICT`。

### 编译库ii

执行`make`按生成的Makefile编译文件

### 用户控制编译选项

使用CMake `OPTION`命令控制选项，注意第28页第5行。

### 安装

> 软件若干部分需要被安装：这一功能由CMake `install`命令来控制。

第34页，代码3行、第6行，和第10行。

### 控制安装目的地

使用`DESTINATION`，建议使用该宏作为相对安装路径，而不是使用绝对路径，比如`/etc`。

在CMake时，设置`CMAKE_INSTALL_PREFIX`值 在安装时，使用`DESTDIR`机制，如： `make DESTDIR=/tmp/testinstrall install`

### 使用CMake变量

## 2. some
