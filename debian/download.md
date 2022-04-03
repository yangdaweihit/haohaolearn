# 安装 

## 镜像
 从[中国科技大学镜像网站](https://mirrors.ustc.edu.cn)下载镜像文件：
 [debian-live-[version]-amd64-gnome.iso](https://mirrors.ustc.edu.cn/debian-cd/current-live/amd64/iso-hybrid)。

## 制作启动u盘

Windows系统使用`UltraISO`或其它类似工具。在Linux系统中，一般使用`dd`命令。

- 插入u盘，查看u盘设备名称。
```
sudo df  # 以/dev/sdc1为例，其挂载点为 /media/wall-e/sony
sudo umount /media/wall-e/sony  # 卸载u盘
```

- 确定u盘的设备名称`sdc`，注意不是分区`sdc1`，写入iso镜像文件 

```
sudo dd if=<xxx.iso> of=/dev/sdc bs=2M
sync # 注意要做同步，确保完成拷贝
```
