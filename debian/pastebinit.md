# 代码粘帖
在很多场景下我们需要将一段信息粘帖出来，比如：
- 请对方检查我的代码；
- 给对方示范程序；
- 请对方了解本地机上的终端信息；
- ...(so many)

# pastebinit

https://help.ubuntu.com/community/Pastebinit

`pastebinit`用于将一大段文本信息上传到网站上，你只需要将网站为你自动生成的网址发给对方，对方就可通过访问网页看到灰常工整的代码或信息了。好处辣么多，废话不说，开始操练吧。

## 安装
```
sudo apt install pastebinit
```

## 使用示例
- 给对方看看源配置
```
cat /etc/apt/sources.list | pastebinit
```
回显出一个网址：`http://paste.debian.net/781180/`，发给对方吧。

- 换个代码帖粘网站
```
cat /etc/apt/sources.list | pastebinit -b paste.ubuntu.com
```

回显出一个网址：`http://paste.ubuntu.com/19346574/`，发给对方吧。

- 其它支持网站

```
> pastebinit -l
Supported pastebins:
- cxg.de
- dpaste.com
- fpaste.org
- lpaste.net
- p.defau.lt
- paste.debian.net
- paste.openstack.org
- paste.pound-python.org
- paste.ubuntu.com
- paste.ubuntu.org.cn
- paste2.org
- pastebin.com
- slexy.org
- sprunge.us
```
