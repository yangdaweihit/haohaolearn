# 源的设置

参考：

- [Debian源使用帮助](https://mirrors.ustc.edu.cn/help/debian.html)

## 源文件
如果遇到无法拉取 https 源的情况，请先使用 http 源并安装：
```
sudo apt install apt-transport-https
```

编译文件：`sudo vi /etc/apt/sources.list`

```
deb https://mirrors.ustc.edu.cn/debian/ bullseye main contrib non-free
deb https://mirrors.ustc.edu.cn/debian/ bullseye-updates main contrib non-free
deb https://mirrors.ustc.edu.cn/debiancn/ bullseye main
deb https://mirrors.ustc.edu.cn/debian-security bullseye/updates main contrib non-free
```
或测试版：
```
deb http://mirrors.ustc.edu.cn/debian/ bullseye main contrib non-free
deb http://mirrors.ustc.edu.cn/debian/ bullseye-updates main contrib non-free
deb http://mirrors.ustc.edu.cn/debian-security bullseye-security main
```


国内还可以选择的镜像网站：

- mirrors.163.comm
- mirrors.tuna.tsinghua.edu.cn


某些源取自launchpad，需要下载密钥
```
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv < PUBKEY >
```

## 源速度测试

- 比较镜像网站

  `sudo netselect ftp.debian.org http.us.debian.org  mirrors.163.com mirros.sohu.com`

- 查找stable版本中最快的镜像网站

  `sudo netselect-apt stable`

