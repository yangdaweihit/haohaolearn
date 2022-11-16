# RESCONTROL

```
RESCONTROL, Action, Ldstep, Frequency, MAXFILES, --, MAXTotalFiles
Controls file writing for multiframe restarts.
```

- Action

    命令动作。合法选项为：

  + DEFINE
  
      默认值，定义一个荷载步中要写入多少个.Xnnn重启动文件。
      
  + FILE_SUMMARY

      列出子步和荷载步的信息。若使用此项，其它参数被忽略。
      
      
- Ldstep


  + ALL
  
      