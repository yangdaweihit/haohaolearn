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

