# 软件

## 配置/etc/fstab

```
<file system>	<mount point>		<type>	<options>	<dump>	<pass>
UUID=xxxxx	/path/to/direcotory	ext4	defaults	0	2
```

获取硬盘分区的UUID:
```
sudo blkid
```

## 示例

# /etc/fstab: static file system information.
#
# Use 'blkid' to print the universally unique identifier for a
# device; this may be used with UUID= as a more robust way to name devices
# that works even if disks are added and removed. See fstab(5).
#
# <file system> <mount point>   <type>  <options>       <dump>  <pass>
# / was on /dev/sda2 during installation
UUID=bb61470c-89dc-4bbb-8132-94adaf355be8 /               ext4    errors=remount-ro 0       1
# /boot/efi was on /dev/sda1 during installation
UUID=C6D7-A6EF  /boot/efi       vfat    umask=0077      0       1
# /home was on /dev/sda4 during installation
UUID=f035d3b6-a125-4e58-b641-b20dee4ef234 /home           ext4    defaults        0       2
# swap was on /dev/sda3 during installation
UUID=14d0c2d3-33f3-4700-864e-004945f8dcd3 none            swap    sw              0       0
# 1TB
UUID=ac8113ca-6c3d-407e-be85-5b75b839871d	/home/wall-e/Documents/ExtDocuments	ext4	defaults	0	2

