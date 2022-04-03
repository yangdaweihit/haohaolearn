# here

找到当前脚本文件所在的路径。

## 安装

```
install.packages("here")
```

## 使用

```
library(here)
# 在当前目录生成.here文件
set_here()
# 获得脚本所在文件夹
setwd(here())
getwd()
```

# 要点

https://github.com/jennybc/here_here#the-fine-print


## 参考

- [Ode to the here package](https://github.com/jennybc/here_here#the-fine-print)
- [github](https://github.com/r-lib/here)
- [Project-oriented workflow](https://www.tidyverse.org/articles/2017/12/workflow-vs-script/)