# PDFTK

`pdftk`是一个处理PDF文件的工具。

## 旋转

- clockwise
```
pdftk input.pdf cat 1-endeast output output.pdf
```

- anti-clockwise
```
pdftk input.pdf cat 1-endwest output output.pdf
```

## 参考

- [Command line: How do you rotate a PDF file 90 degrees?](mindhacks.cn/2008/09/21/the-magical-bayesian-method/)