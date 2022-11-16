# *MOPER

```
*MOPER, ParR, Par1, Oper, Val1, Val2, Val3, Val4, Val5, Val6
Performs matrix operations on array parameter matrices.
```

- ParR

    结果向量参数矩阵。
    
- Par1

    第1个输入算子的向量参数矩阵。
    
- Oper

  + INVERT
  
      `*MOPER, ParR, Par1, INVERT`
      
      计算逆矩阵。矩阵必须是良性的，病态矩阵或有相关列矩阵将产生错误。
        
  + MULT
  
      `*MOPER, ParR, Par1, MULT, Par2`
      
      矩阵乘：Par1 x Par2， Par1列数要等于Par2行数。若Par2行数大于Par1列
      数，矩阵依然相乘，但多余行数不被计入运算中。
      
  + COVAR
   
       `*MOPER, ParR, Par1, COVAR, Par2`
       
       自方差矩阵：度量输入矩阵Par1各列的关联程度。
       
  + CORR
  
       `*MOPER, ParR, Par1, CORR, Par2`
       
       相关性矩阵：度量输入矩阵Par1t各列的相关性系数。
       
  + SOLV

       `*MOPER, ParR, Par1, SOLV, Par2`
       
       解方程组：Par1 x ParR = Par2，Par1必须是方阵。方程必须是线性、独
       立、和良性的。
       

其它功能尚不理解。

## 代码示例

```
!----------------------------------------------------------------------
! math.inp
! 矩阵操作示例
! 定义向量p和矩阵grad
! 求解 grad*x=p
! 计算 grad逆矩阵ingrad
! 计算 pp = grad*x
!
! yangdawei
! HIT
! 08/02/2015
!----------------------------------------------------------------------

fini
/clear

*dim,grad,,2,2
*dim,p,,2
!*dim,x,,2        !结果向量亦可不定义
!*dim,ingrad,,2,2 !结果向量亦可不定义

p(1)=2
p(2)=3

grad(1,1)=1.0
grad(1,2)=2.0
grad(2,1)=1.0
grad(2,2)=4.0

*moper,ingrad,grad,invert
*moper,x,grad,solv,p
*moper,pp,grad,mult,x

*mwrite,grad,grad,txt,,jik,2,2
(2f10.3)

*mwrite,ingrad,ingrad,txt,,jik,2,2
(2f10.3)

*cfopen,result,txt
*vwrite,p(1),pp(1),x(1)
(3f10.3)
*cfclos
```

## 参考

- [帮助系统](http://www.mm.bme.hu/~gyebro/files/ans_help_v182/ans_cmd/Hlp_C_MOPER.html)
   
  
    
    
