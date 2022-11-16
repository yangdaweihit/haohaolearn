# 杂项

## i386

增加框架
```
sudo dpkg --add-architecture i386
```

删除框架
```
sudo apt-get purge ".*:i386"
sudo dpkg --remove-architecture i386
```

## Trackpoint和Touchpad未启动

```
sudo modprobe -r psmouse
sudo modprobe psmouse proto=imps
```

## 缺少固件

首先安装非自由固件驱动：
```
sudo apt install firmware-misc-nonfree 
```

若有`i915`固件缺失，则先找到固件，比如：

```
W: Possible missing firmware /lib/firmware/i915/icl_dmc_ver1_07.bin for module i
915
W: Possible missing firmware /lib/firmware/i915/tgl_dmc_ver2_04.bin for module i
915
W: Possible missing firmware /lib/firmware/i915/bxt_huc_ver01_8_2893.bin for mod
ule i915
```

1. 建立文件夹
```
sudo mkdir -p /lib/firmware/i915
```

2. 拷贝相应的固件[i915](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/plain/i915)

3. 重新配置`initramfs-tools`包

```
sudo dpkg-reconfigure initramfs-tools
```

## 休眠时需要授权

弹出对话框提示：`Authentication is required for suspending the system`。

将当前用户加入到`users`群中：
```
sudo usermod -aG users "$USER"
```

若Polkit版本低于0.106：

增加文件：
`/var/lib/polkit-1/localauthority/50-local.d/50-enable-suspend-on-lockscreen.pkla`
：

```
[Allow suspending in lockscreen]
Identity=unix-group:users
Action=org.freedesktop.login1.suspend
ResultAny=yes
ResultInactive=yes
ResultActive=yes
```

设定权限：
```
sudo chmod 644 /var/lib/polkit-1/localauthority/50-local.d/50-enable-suspend-on-lockscreen.pkla
```

## 消除麦克回声

```
sudo vi /etc/pulse/default.pa
load-module module-echo-cancel
pulseaudio -k
pulseaudio --start
```

- [Background Noise Cancelling](https://somtips.com/remove-background-noise-of-microphone-on-linux-system/)

## 参照

- [Touchpad not working after Debian Buster clean install](https://www.reddit.com/r/debian/comments/compbe/touchpad_not_working_after_debian_buster_clean/)

- https://askubuntu.com/questions/811453/w-possible-missing-firmware-for-module-i915-bpo-when-updating-initramfs

- [Authentication required before suspend](https://askubuntu.com/questions/543921/authentication-required-before-suspend)