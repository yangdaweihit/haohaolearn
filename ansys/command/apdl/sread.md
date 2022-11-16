# *SREAD

```
*SREAD, StrArray, Fname, Ext, --, nChar, nSkip, nRead
Reads a file into a string array parameter.
```

- StrArray

    向量参数名。
    
- Fname

    文件名和目录路径(总长不得大于248个字符)。
    
- Ext

    扩展名。
    
- nChar

    每行字符数(默认为文件中最长行的长度)。
    

- nSkip

    从文件开始跳过的行数(默认为0)。

- nRead

    读入的行数(默认为全部文件)。
    

## 代码示例

```
*sread, text, math, inp
! 在监视窗口输出第14行
! 文件中每一行存至text的每一列中
/com, %text(1,14)%
```

## 参考

- [帮助系统](http://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_cmd/Hlp_C_SREAD_st.html)
   
  
    
    
