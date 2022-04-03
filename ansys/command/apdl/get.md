# GET

```
*GET, Par, Entity, ENTNUM, Item1, IT1NUM, Item2, IT2NUM
Retrieves a value and stores it as a scalar parameter or part of an array parameter.
```

- Par

    结果参数名。
   
- Entity

    条目关键字。合法关键字：`NODE`，`ELEM`，`KP`，`LINE`，`AREA`，
    `VOLU`等，见`Entity=`表。
   
- ENTNUM

    对应条目的数字或标签，见`ENTNUM=`表。
    
- Item1

    给定条目的特定项名称。合法项见表中的`Item1`表。
    
- IT1NUM

    特定项对应的数字或标签。
    
- Item2, IT2NUM

    第2项。
    
## Entity = ELEM

```
Entity = ELEM, ENTNUM = N (element number) 
*GET,Par, ELEM, N, Item1, IT1NUM, Item2, IT2NUM
```

| Item1 | IT1NUM | 描述                                 |
|-------|--------|--------------------------------------|
| SMISC | Snum   | 单元顺序号Snum号对应的可加杂项数据值 |

    
## 参考

- [帮助系统](http://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_cmd/Hlp_C_GET.html#gettabgen)