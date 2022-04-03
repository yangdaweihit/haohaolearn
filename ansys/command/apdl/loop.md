# 循环结构

## DO

```
*DO, Par, IVAL, FVAL, INC
Defines the beginning of a do-loop.
```

- 以`*ENDDO`结尾。
- `Par`为循环变量。
- `IVAL`初始值。
- `FVAL`终止值。
- `INC`循环变量增量值。

## DOWHILE

```
*DOWHILE, Par
Loops repeatedly through the next *ENDDO command.
```

- 以`*ENDDO`结尾。
- 只要Par大于零，便重复执行循环体内代码。

## *EXIT

退出循环，执行`*ENDDO`之后的代码。

## *CYCLE

忽略其后，`*ENDDO`之前的代码，继续循环。

## 参考

- [帮助系统](http://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_cmd/Hlp_C_DO.html)

