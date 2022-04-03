# zip/unzip

## 中文乱码

默认的unzip无法解析中文编码，致使Windows下压缩的zip文件在解压时出现乱码。为此，有人开发了[unzip-iconv](https://github.com/m13253/unzip-iconv)，该软件已被打包收在`debiancn`仓库中。
```
sudo apt install unzip-iconv
unzip -O GB18030 xxx.zip
```

```
wget https://mirrors.ustc.edu.cn/debiancn/debiancn-keyring_0\~20161212_all.deb
sudo dpkg -i debiancn-keyring_0~20161212_all.deb
echo "deb https://mirrors.ustc.edu.cn/ stretch main" | sudo tee /etc/apt/sources.list.d/debiancn.list;
sudo apt update
sudo apt install unzip-iconv
```

