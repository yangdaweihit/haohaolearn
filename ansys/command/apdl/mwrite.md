# *MWRITE

```
*MWRITE, ParR, Fname, Ext, --, Label, n1, n2, n3
Writes a matrix to a file in a formatted sequence.
```

- ParR

    向量参数名。
    
- Fname

    文件名和目录路径(总长不得大于248个字符)。
    
- Ext

    扩展名。
    
- Label

    可以是`IJK`，`IKJ`，`JIK`，`JKI`，`KJI`，或空(即JIK)。这个标签定义了
    打印顺序。默认为`JIK`，即指对于2维数组，先沿列方向循环，即先固定行数，
    按列指标循环输出元素。简言之，即逐行输出。
    

- n1, n2, n3

    `(((ParR(i,j,k), k = 1,n1), i = 1, n2), j = 1, n3)`若`Label = KIJ`。
    默认为对应维度的长度。
    
## 注释

和`*VWRITE`一样，在其之后紧跟格式化语句。格式化描述符为Fortan或C格式。

Fortan格式符包含在括号中。整型I和列表*描述符不能使用。其它示例如`(4F6.0,
8A), (E10.3,2X,D8.2)`

若第一个描述符不是左括号，则按C语言格式化解释。`%I`用于整数，`%G`用于双
精度型，`%C`用于字符，`%/`用于断行，`%X`用于空格。

详细解释见
[*MSG](http://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_cmd/Hlp_C_MSG.html)

## 代码示例

```
*dim, m,,2,3

m(1,1) = 1
m(1,2) = 2
m(1,3) = 3
m(2,1) = 4
m(2,2) = 5
m(2,3) = 6

*mwrite,m,m,txt,,jik
(3f10.3)
```

## 参考

- [帮助系统](http://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_cmd/Hlp_C_MOPER.html)
   
  
    
    
