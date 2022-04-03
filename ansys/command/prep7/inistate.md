# INISTATE

```
INISTATE, Action, Val1, Val2, Val3, Val4, Val5, Val6, Val7, Val8, Val9
Defines initial state data and parameters.
```

- Action 

    规定定义或操作初始状态数据的动作。
    
    + SET
    
        指定初始状态坐标系，数据类型，材料类型参数。
        
    + DEFINE
    
        定义实际状态值，和相应的单元，积分点，或层信息。
        
    + WRITE
    
        当SOLVE命令执行时，将初始状态写入文件。
        
    + READ
        
        从文件读入初始状态。
        
    + LIST 
    
        读出初始状态。
        
    + DELETE
       
       删除所选择单元的初始状态。
    
- Val1, Val2, ..., Val9 

    基于Action类型的输入值。
    
## 代码示例

```
!定义第31单元的初始应变为0
! 首先定义坐标系为-2，即单元初始状态
! 定义数据类型为epel，即初应变
! 定义31初始状态数值为0
inis,set,csys,-2
inis,set,dtyp,epel
inis,define,31,,,,0
```

## 参考

- [帮助系统](http://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_cmd/Hlp_C_ENGEN.html)
- 注意：该帮助中的首个参数IINC事实上是不存在的。