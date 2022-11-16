# Birth & Death

## EALIVE

```
EALIVE, ELEM
Reactivates an element (for the birth and death capability).
```

- ELEM

    要激活的单元。 若ALL，激活所有已选单元(ESEL)。
    
###  注释

- 单元只有被杀死后才能激活。
- 被激活的单元具有零应变状态。
- 不能在时效材料分析中使用激活/杀死功能，如粘弹、粘塑、徐变分析。
- 该命令亦可以PREP7层使用。

## EKILL

```
EKILL, ELEM
Deactivates an element (for the birth and death capability).
```

- ELEM

    要杀死的单元。 若ALL，激活所有已选单元(ESEL)。

###  注释

- 被杀死单元依旧在模型中，但几乎不贡献刚度，值由ESTIF设定。
- 任何依赖于解的量设定为0(如应力、塑性应变，徐变应变等)。
- 被杀死单元不贡献质量，也不生成荷载向量。

## ESTIF

```
ESTIF, KMULT
Specifies the matrix multiplier for deactivated elements.
```

- KMULT

    刚度矩阵因子，默认1.0E-6。