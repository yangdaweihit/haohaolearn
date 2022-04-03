# 休眠

## 背景

通常只有当swap分区大于内存时才能正常休眠。然而我的系统swap仅设为4G，而内
存是12G。为了实现休眠，采用在硬盘上定义swap文件的方法。

## 步骤

1. 定义swapfile，大小宜大于内存：

```
sudo fallocate -l 16g /swapfile # 我的机子是16G，具体自己修改
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
echo '/swapfile swap swap defaults 0 0' | sudo tee -a /etc/fstab
```

2. 安装用户空间软休眠`Userspace Software Suspend`包

```
sudo touch /etc/uswsusp.conf
sudo dpkg-reconfigure -pmedium uswsusp
```

进入配置窗口后，一路下一步即可，中间需要设置密码，配上系统密码即可。经以
上修改，即可实现正常休眠。参考帖中又修改了`systemd`的`hibernate`服务。我
如法操作后，反而无法进入休眠，屏幕只是闪灭一下回复到初始状态。后又删去了
`/etc/systemd/system/systemd-hibernate.service.d/override.conf`。


## 参考

- https://blog.justforlxz.com/2018/12/12/hibernate-for-swapfile/
- https://askubuntu.com/questions/6769/hibernate-and-resume-from-a-swap-file
- https://wiki.archlinux.org/index.php/Uswsusp