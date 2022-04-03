# /INQUIRE

## 查询系统信息

```
/INQUIRE, StrArray, FUNC
Returns system information to a parameter.
```
- StrArray

    是一个字符数组型字符串，该字符串同于字符参数数组，只是每个单元可有
    248个字符。若参数未定义，可新生成。

- FUNC

    定义了需返回的系统信息

  + LOGIN

    返回Linux系统的登录路径名或Windows系统的默认路径（包括磁盘符）。

  + DOCU

    ANSYS的文档目录路径。

  + APDL

    ANSYS APDL目录路径。

  + PROG

    ANSYS可执行程序路径。

  + DIRECTORY

    当前文件夹路径。

  + JOBNAME

    返回当前Jobname。
  
## 返回文件参数

`/INQUIRE`命令亦可返回系统中特定文件的信息，格式为：

```
/INQUIRE,Parameter,FUNC,Fname, Ext, --. 
```

- FUNC

  + EXIST

    若文件存在返回1，若不存在返回0。

  + DATE

    以`yyyymmdd.hhmmss`形式返回文件时间戳。

  + SIZE

    以MB返回文件大小。

  + WRITE
  
    返回文件写入特性: 1表示可写，0表示不可写。

  + READ

    返回可读特性：1表示可读，0表示不可读。

  + EXEC

    返回可执行特性：1表示可执行，0表示不可执行。

  + LINES

    返回ASCII文件行数。
    
## 代码示例

```
! 查询文档是否存在，若存在则删除
/inquire,isexist,exist,import_record,log
*if,isexist,eq,1,then
    /delete,import_record,log
*endif

! 查询文档行数，并按行数定义数组
/inquire,my_lines,lines,sectionname,txt
*dim,secfile,string,8,my_lines

*sread,secfile(1),sectionname,txt
```
  

## 参考

- [帮助系统](http://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_cmd/Hlp_C_INQUIRE.html)