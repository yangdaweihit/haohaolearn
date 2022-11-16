# SESSION命令

进程命令用于提供通用控制功能。

## 运行控制

### /CWD
```
/CWD, DIRPATH
Changes the current working directory.
```

### /EXIT

```
/EXIT, Slab, Fname, Ext, --
Stops the run and returns control to the system.
```

- Slab
  + MODEL: 仅保存模型(默认)。
  + SOLU: 保存模型和解数据。
  + ALL: 保存模型、解，和后处理数据。
  + NOSAVE: 不在File.DB上保存数据（当前File.DB不被替代）。

- Fname：文件名，默认为`Jobname`。
- Ext: 扩展名（最多8位），若为空则默认为`DB`。
  

## 处理层

- FINISH
- /PREP7
- /POST1
- /POST26
- /QUIT
- /SOLU


## 文件

### /COPY

```
/COPY, Fname1, Ext1, --, Fname2, Ext2, --, DistKey
Copies a file.
```


## 列表控制

### /COM

```
/COM, Comment
Places a comment in the output.
```

将注释置于输出文件中。

- Comment

注释字符串，最多75个字符。

## 参考

- [帮助系统](http://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_cmd/Hlp_C_CH2_1.html)