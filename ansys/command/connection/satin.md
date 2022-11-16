# ~SATIN

```
~SATIN, Name, Extension, Path, Entity, FMT, NOCL, NOAN
Transfers a .SAT file into the ANSYS program.
```

- Name: .SAT文件名。
- Extension: 扩展名，默认为.sat。
- Path: 路径名，应包含在单引号中。默认为当前工作目录。
- Entity: 引入的实体。
  + SOLIDS：只有实体，引入作为ANSYS体。
  + SURFACES: 只有面，引用作为ANSYS面。
  + WIREFRAME：只有线框，引用作为ANSYS线。
  + ALL: 所有实体。
- FMT: ANSYS存储格式。
  + 0: Neutral格式（默认）。
  + 1: 实体格式。
- NOCL: 去除小对象。
  + 0: 去除微小对象，不检查模型完整性（默认）。
  + 1: 不去除微小对象。


## 参考

- [帮助系统](http://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_cmd/Hlp_C_SATIN.html)