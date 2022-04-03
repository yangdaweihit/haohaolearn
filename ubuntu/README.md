# Ubuntu

## 下载和源
- mirrors.163.com
- 页面上有`获取安装镜像`的按钮，选择安装发行版Ubuntu，选择倾向的版本，点击`获取ISO`按钮。
- 源配置示例(19.04)：`/etc/apt/sources.list`
``` 
deb https://mirrors.163.com/ubuntu/ eoan main restricted universe multiverse
deb https://mirrors.163.com/ubuntu/ eoan-security main restricted universe multiverse
deb https://mirrors.163.com/ubuntu/ eoan-updates main restricted universe multiverse
deb https://mirrors.163.com/ubuntu/ eoan-backports main restricted universe multiverse
```

## 将capslock设置为ctrl
- 编辑`/etc/profile`
- /usr/bin/setxkbmap -option "ctrl:nocaps"
 
## PATH 

修改路径的命令如下：
```
PATH=$PATH:~/.local/bin;
export PATH
```
为了使其生效，应将该命令放在配置文件中。
- `/etc/enviornment`：对所有用户生效
- `/etc/profile`：对所有用户生效
- `.bashrc`: 对当前用户生效
- `.zshrc`：当zsh作为用户登录时的shell时，应置于该文件中。

## 启动时自动执行脚本 

`/etc/rc.local`

```
#! /bin/sh 
ssr
exit 0
```

`sudo chmod +x /etc/rc.local`

## 重命名

安装`rename`

例如重命名`[NS]D[1-13]索力时程.png`为`[NS]D[1-3].png`：

```
rename 's/索力时程//' *.png
```

## unzip

- [字符集](https://www.iana.org/assignments/character-sets/character-sets.xhtml)
- [以特定字符集解压](https://superuser.com/questions/872596/decompress-zip-with-given-encoding)

- 示例：
```
unzip -O GB18030 xxx.zip -d target_dir
```

## iconv

- 查看文档编码
```
file -i xxx.srt
```

- [转换命令](https://www.tecmint.com/convert-files-to-utf-8-encoding-in-linux/)
- 示例
```
iconv -f GB18030 -t UTF-8 xxx.rst -o xxx_utf8.rst
```

## 网易云音乐

```
sudo vi /usr/share/applications/netease-cloud-music.desktop
Exec=sh -c "unset SESSION_MANAGER && netease-cloud-music %U"
```

## GNOME Extensions

- OpenWeather
- Dash to Doc
- Caffeine
- Sound Input & Output Device Chooser
- Center Area Horizontal Spacing
- Hide Activities Button
- Status Area Horizontal Spacing
- TopIcons Plus
- TopIcons Redux
- Transparent Top Bar