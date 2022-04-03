# SFBEAM

```
SFBEAM, Elem, LKEY, Lab, VALI, VALJ, VAL2I, VAL2J, IOFFST, JOFFST, LENRAT
Specifies surface loads on beam and pipe elements.
```

- Elem

    要施加表面荷载的单元。若为ALL，则施加于所有已选择单元。

- LKEY

    荷载键值(默认为1) 。对于每种单元的荷载键值见单元手册。对于梁和一些管
    单元，荷载键值代表了荷载方向。
    
- Lab

    表面荷载标签。结构标签：PRES(压力)。
    
- VALI, VALJ

    在I和J节点处的表面荷载值。若VALJ为空，则默认等于VALI。若为0，则表示0
    值。
    
- VAL2I, VAL2J

    在I和J节点处的表面荷载第2个值。现在未应用。
    
- IOFFST, JOFFST

    从I和J节点偏移的距离为荷载作用范围。
    
- LENRAT

  + 0
      
      用长度单位偏移(默认)。
      
  + 1
  
      用长度比例偏移(0.0到1.0)。

## 参考

- [帮助系统](http://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_cmd/Hlp_C_SFBEAM.html)