# PDF

## 压缩

扫描版的文件一般较大，压缩方法
```
gs -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=setting -sOutputFile=output.pdf input.pdf
```

### setting选项：
- /screen: 最低分辨率，最小； 
- /ebook: 中度分辨率；
- /printer, /prepress: 较高清晰度，适用于打印。


### python脚本

- 有人提供了现成的[python脚本](https://github.com/theeko74/pdfc)。