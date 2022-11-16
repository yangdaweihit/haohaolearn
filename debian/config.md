# 配置

## 源配置 

- [源的设置](sources.md)

## 安装并配置`sudo`

安装`sudo`可方便软件安装和配置

```
su
apt update
apt install sudo
chmod +w /etc/suders
vi /etc/sudoers
```

在`sudoers`中填加`<用户名>`的权限

```
<用户名>  ALL=(ALL) ALL
```

## 显卡配置

### 查看显卡驱动

```
sudo apt install lshw
suo lshw -c video
```

### 英伟达显卡驱动
```
sudo apt install nvidia-detect nvidia-driver
```

## 语言配置

- 一般安装时应选择系统语言时为英文，稍后还要安装上中文编码：

  `sudo dpkg-reconfigure locales`

  在弹出的的对话框中选择`zh_CN.UTF-8`、`zh_CN.GB2312`等，按SPC确认。

- 但这会使得稍后在Emacs中无法输入中文。
  因此需要编辑`/etc/default/locale`：

```
LANG=en_US.UTF-8
LC_CTYPE=zh_CN.UTF-8
```


## 字体配置

Adobe公司提供的开源字体： 
- [思源无衬线](https://github.com/adobe-fonts/source-han-sans/tree/release)，
- [思源有衬线](https://github.com/adobe-fonts/source-han-serif/tree/release)


有时系统内未安装目标字体，系统会自动将既有字体与目标字体对比，将最接近的字体替换目标字体。编辑`fonts.conf`即可人工配置替换字体。
```
vi .config/fontconfig/fonts.conf
```

```
<?xml version="1.0"?>
<!DOCTYPE fontconfig SYSTEM "fonts.dtd">
<fontconfig>

  <match target="pattern">
    <test name="family" qual="any" >
      <string>Times</string>
    </test>
    <edit name="family" mode="assign" binding="strong">
      <string>Times New Roman</string>
    </edit>
  </match>

  <match target="pattern">
    <test name="family" qual="any" >
      <string>Courier</string>
    </test>
    <edit name="family" mode="assign" binding="strong">
      <string>Free Courier</string>
    </edit>
  </match>

</fontconfig>
```

## 安装中文字体

安装开源中文字体，方便中文显示。

```
sudo apt install fonts-wqy-zenhei
```

## 配置中文编码

```
sudo dpkg-reconfigure locales 
```

选择`zh_CN.UTF-8`(SPACE切换选择)，确认退出。

## 中文输入

```
sudo vi /etc/default/locale
```

```
LANG=en_US.UTF-8
LC_CTYPE="zh_CN.UTF-8"
```

```
sudo update-locale
```

## 时区

```
sudo dpkg-reconfigure tzdata
```

选择本地城市。

## 交换`Caps Lock`与`Ctrl`

```
sudo vi /etc/default/keyboard
```

```
XKBOPTIONS="ctrl:nocaps"

```

# 自动登录和列出用户

- [LightDM](https://wiki.debian.org/LightDM) 
- `/etc/lightdm/lightdm.conf`
```
[Seat:*]
autologin-user=<username>
```
将用户名加入`autologin`组：
```
sudo groupadd autologin
sudo gpasswd -a <username> autologin
```

- `/usr/share/lightdm/lightdm.conf.d/01_my.conf`
```
[Seat:*]
greeter-hide-users=false
```

- `/etc/lightdm/lightdm-gtk-greeter.conf`
```
[greeter]
theme-name=Numix
icon-theme-name=Faenza-Ambiance
```

# 登录届面订制

使用`lightdm-settings`

# crontab

启机时自动执行脚本，需要`root`权限。

```
sudo crontab -e
```
填加：
```
@reboot bash /path/to/script.sh
```


# 安装打印机

```
sudo apt install printer-driver-all system-config-printer
```
参考：[SystemPrinting](https://wiki.debian.org/SystemPrinting)

# 锁屏

1. 有`xflock4`配以`Ctrl-Alt-Delete`默认功能
2. 写脚本配上快捷键

```
#!/bin/bash
sleep 1; xset dpms force off
```


参考：[How to turn off screen with shortcut in Linux](https://superuser.com/questions/374637/how-to-turn-off-screen-with-shortcut-in-linux)

