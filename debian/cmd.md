# CMD

- [Linux命令大全](man.linuxde.net)

## Linux系统中分区格式化u盘

1. 查看u盘设备名称

   > sudo fdisk -l

2. 查看符合u盘空间的设备，确定设备名称，如`/dev/sdb`。

3. 在u盘设备上建立分区

   > sudo fdisk /dev/sdb

   进入`fdisk`界面后，使用命令建立分区：

   - m: 查看命令清单
   - n: 建立分区
   - t: 转换分区类型，`07`表示`NTFS`分区
   - w：写入分区

4. 格式化

   > sudo mkfs.ntfs -f /dev/sdb1

## mkntfs

- 建立一个NTFS文件系统
- 隶属于`ntfs-3g`包
- 应用：
  + 查看确认待格式化的分区：`sudo fdisk -l`
  + 以`sdb1`为例：`sudo mkntfs -f /dev/sdb1`
  + `-f`代表快速，亦可为`--fast`、`--quick`、`-Q`
- 参考：https://linux.die.net/man/8/mkfs.ntfs

## mkfs

- 建立一个Linux文件系统
- 隶属于`util-linux-ng`包
- 应用：`sudo mkfs -t ext4 /dev/sdb1`
- 参考：https://linux.die.net/man/8/mkfs

## du

- `du -sh [dir]`

## ncdu

- 查看磁盘用量
- 语法：`ncdu [options] dir`
  + options: 选项
  + dir: 扫描指定目录
- 示例：`ncdu /`
- 进入窗口后，由`KEYS`实施操作：
  + up, down, j, k: 遍历
  + right, enter, l: 打开选择的目录
  + left, <, h:  返回父目录
  + n: 以filename排序，再按一下变为降序(下同)
  * s: 以filesize排序
  * C: 以文件数排序
  * a: 在用量和相对大小间切换
  + 其它详见`man`

## dpkg 

dpkg是Debian的软件管理器(也许是Debian PacKaGe的辅音字母缩写)，用于安装、
编译、卸载和管理Debian的软件。dpkg的前台软件为`aptitude`。

dpkg保存着可用包的信息，包括三类：`states`，`selection states`，`flags`。


## apt 

- `-f`,`--force`
    强制安装，解决依赖包的安装。

- `–no-install-recommends`
    避免安装推荐的包。

### apt-cache

apt-cache对APT包进行查询输出。

- 查找<package-name>的依赖包
```
apt-cache depends <package-name>
```
- 查找<package-name>被哪些包依赖
```
apt-cache rdepends <package-name>
```

## 系统查询

- 查看系统版本
```
lsb_release -a
```
- 查看内核版本
```
uname -a
```

- 查看硬件

| 命令            | 用途           |
|-----------------|----------------|
| `lscpu`         | 查看CPU信息    |
| `lspci`         | 查看PCI设备    |
| `sudo fdisk -l` | 查看分区       |
| `df -h`         | 查看磁盘信息   |
| `lsmod`         | 当前加载的驱动 |

- 查看显卡型号
```
lspci | grep -i vga
sudo lshw -numeric -class video # 使用lshw
nvidia-smi #如果知道是NVIDIA显卡，还可以使用命令：
```

- 查看声卡型号
```
lspci |grep -i audio
cat /proc/asound/cards
```

- 查看网卡型号
```
lspci | egrep -i 'network|ethernet'
lshw -class network
```

- 查看网络设备
```
ip a
```


## xclip

- 将当前目录拷贝至粘贴板，进入粘贴板中所存的目录，将该目录写到文件中。

```
pwd | xclip
cd $(xclip -o)
xclip -o > ~/test.txt
```

## 查看启动中的错误

```
sudo dmesg | grep <错误信息关键字>
```


## apt-mark
标记`sudo`为手动安装，避免因其它程序卸载而被连带卸载。
```
  apt-mark manual sudo
```
## 日志查看

```
sudo journalctl -b | grep -i failed
```

## 启动错误修复 

```
debian kernel: [Firmware Bug]: TSC_DEADLINE disabled due to Errata; please update microcode to version: 0x52 (or later)
sudo apt-get install intel-microcode
```
