# D

```
D, Node, Lab, VALUE, VALUE2, NEND, NINC, Lab2, Lab3, Lab4, Lab5, Lab6
Defines degree-of-freedom constraints at nodes.
```

- Node

    定义约束的节点。若为ALL，则NEND和NINC被忽略，约束作用于所有选择节点
    (NSEL)。

- Lab

    - Structural labels

        UX, UY, or UZ (位移); ROTX, ROTY, or ROTZ (旋转); WARP (翘曲)。

    - Value

        约束值。

    - Value2

        第2个约束值(若有)。

    - NEND, NINC

       定义同样约束的节点范围，NEND为范围起点，NINC为增量。

    - Lab2, Lab3, Lab3, Lab4, Lab5, Lab6

       其它约束标签。
  
## 代码示例

```
! 通常不指定约束值，此时标签之间有4个默认量，5个逗号分隔
D,1,UX,,,,,UY,UZ,ROTX,ROTY
D,31,UY,,,,,UZ,ROTX,ROTY
```


## 参考

- [帮助系统](http://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_cmd/Hlp_C_D.html)