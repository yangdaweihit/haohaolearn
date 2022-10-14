# Shotcut

[Shotcut](https://www.shotcut.org/)是一款轻量级视频编辑软件。

## 下载

- https://www.shotcut.org/download/
- Windows: 64-bit Windows installer
- Linux: 64-bit Linux AppImage

## Linux安装

- 将镜像文件赋予可执行权限；
- 在`/usr/bin/`中建立对应的软连接；
- 在`.local/share/applications/`中建立对应的快捷方式文件；
- 下载图标存于`.icons`中，在快捷方式文件中输入该文件名。
- 在Linux中运行界面无法适应显示屏，需要修改其快捷方式中的运行命令：

```
Exec=env QT_AUTO_SCREEN_SCALE_FACTOR=0 sh -c "<path to shotcut>/shotcut "%F""
```

## 教学

- [Shotcut教程](https://www.bilibili.com/video/av77105895?from=search&seid=409103892336391604)