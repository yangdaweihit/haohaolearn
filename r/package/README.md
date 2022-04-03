# 宏包
## 文档
 - [R-exts.pdf](https://cran.r-project.org/doc/manuals/R-exts.pdf)
    
## 编译
 - `package.skeleton`生成宏包目录
 - 修改`man`中所有文件，`title`内容作修改。
 - 终端下检核文件：`R CMD check <package name>`
 - 编译：`R CMD build <package name>`，生成`<package name>_<version>.tar.gz`
      