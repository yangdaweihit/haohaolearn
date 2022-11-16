# EGEN

```
ENGEN, ITIME, NINC, IEL1, IEL2, IEINC, MINC, TINC, RINC, CINC, SINC, DX, DY, DZ
Generates elements from an existing pattern.
```

- ITIME, NINC

    复制ITIME次，包括被拷贝单元。所有节点増量为NINC。若要让复制发生，
    ITIME > 1。
    
- IEL1, IEL2, IEINC

    生成单元范围，从IEL1到IEL2，增量为IEINC。

## 参考

- [帮助系统](http://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_cmd/Hlp_C_ENGEN.html)
- 注意：该帮助中的首个参数IINC事实上是不存在的。