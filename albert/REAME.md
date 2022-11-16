# Albert

## 项目

- [github](https://github.com/albertlauncher/albert)

## 安装

- 来源：[home:manuelschneid3r](https://software.opensuse.org/download.html?project=home:manuelschneid3r&package=albert)

- 在`/etc/apt/sources.list'`中填加：

  ```
  deb http://download.opensuse.org/repositories/home:/manuelschneid3r/Debian_Testing/ /
  ```

- 更新安装

  ```
  wget -nv https://download.opensuse.org/repositories/home:manuelschneid3r/Debian_Testing/Release.key -O Release.key
  apt-key add - < Release.key
  apt-get update
  apt-get install albert
  ```

  

