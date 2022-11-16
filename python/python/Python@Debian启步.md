# Python@Debian启步

![Other-python-icon](/home/wall-e/Desktop/python-icon.png)

本文对在Debian/Linux环境中Python编程做了实际操作方面的说明，便于初学者启步。本文假定读者了解Debian/Linux的基础知识。

## 安装Python

这一步基本不需要，因为Debian已经预装了Python2和Python3。如果真的没有，那就安装一下吧。

```
sudo apt install python python3
```

## Pip

### 安装pip

[pip](https://pip.pypa.io/en/stable/)是Python的包管理器。要了解pip，应阅读其官方文档：https://pip.pypa.io/en/stable/。这里只是将最基本的操作给出说明。

安装pip有两种方式：

- 由脚本文件`get-pip.py`：

```
# 这一步是下载get-pip.py文件
# 若下载时速度太慢，可用链接：链接: https://pan.baidu.com/s/1CbNo9Tl6yDZpZ03Sr8uC5A  密码: p811
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# 运行这个脚本文件
python get-pip.py
```

- 由Debian库：

```
sudo apt-get install python-pip
```

该方法目前在我的系统中不能用。因为我的系统版本为`Bullseye`，该包已不在软件库之中。原因是显然的，Debian从Bullseye已默认不支持Python2，所以pip也就不在支持之列了。以后我们常态下会使用后面要讲到的`pip3`。

### 找到pip

很多人遇到找不到pip命令的问遇：

```
command not found: pip
```

这是因为pip被安装后默认在`~/.local/bin`文件夹中，它恰好不在你的路径(PATH)中。我们需要对PATH略作修改：

```
# 在你的终端配置文件中增加一行
export PATH="~/.local/bin:$PATH"
```

退出终端后再进入，即可使该修改生效。关于这个动作，还要做以下说明：

- 应该在哪个终端配置文件取决于你默认的shell。如果你使用的是bash，则文件应为`.bashrc`；若为zsh，则应为`.zshrc`，其它应通过阅读相应的手册了解配置文件。
- 代码中的`=`左右不应有空格。

### 镜像设置

pip默认从官方服务器(https://pypi.org/)获取库包，这使得我们访问起来很慢。我们可以设置镜像解决这个问题。

编辑`.pip/pip.conf`文件（没有的话就创建一个），这里使用清华的镜像：

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

### 升级pip

在实现了终端中可运行pip后，首先宜将它升级到最新版本：

```
pip install -U pip
pip --version
```

### 管理包

尝试一下安装一个包：

```
# 安装库包
pip install numpy
# 查看该库包的版本
pip list | grep numpy
```

库包默认安装在：`~/.local/lib/`中，但具体位置还要细化，这取决于该包隶属的Python版本，若该库包的隶属于Python3.8，则具体位置为：`~/.local/lib/python3.8/site-packages`。

如果在安装包时使用了`sudo`，即`sudo pip install numpy`，则该包会安装在系统环境中。但如果你现在还执行不了，因为`pip`安装在了用户的`home`路径下。后面讲到了`pip3`则可以执行`sudo pip3 install numpy`。

其它详细信息，请阅读pip手册：

```
man pip
```

## Pip3

`pip3`是pip的Python3版本。

- 安装pip3

  ```	
  sudo apt-get install python3-pip 
  ```

- 由pip3安装库包

  ```
  # 参数 --user 用于采用用户方案安装；如果不加上，系统亦会概据该命令没有使用sudo而默认采用该参数。
  pip3 install --user numpy
  ```

  

# VirtualEnv

(todo)

## Emacs 环境配置

(todo)

## Visual Studio Code 环境配置

(todo)

## Todo

- [x] pip
- [x] pip3
- [ ] VirtualEnv
- [ ] Emacs环境配置
- [ ] Visual Studio Code环境配置

