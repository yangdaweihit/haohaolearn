# TeXLive

## 下载

- 由[科大镜像地址](https://mirrors.ustc.edu.cn/CTAN/systems/texlive/Images/)下载texlive[xxx].iso

## 安装

- 安装显示界面需要的库
```
sudo apt install perl-tk
```

- 加载镜像

```
sudo mount texlive[xxx].iso /mnt
```

- 安装

```
cd /mnt
sudo ./install-tl --gui
```

出现界面后一路下一步即可。

- 卸载镜像

```
sudo umount /mnt
```
