# 配置

## 设置镜像

- 镜像列表：https://cran.r-project.org/mirrors.html
- 配置文件：`/etc/R/Rprofile.site`或`.Rprofile`(推荐)：

```
local({
  r <- getOption("repos")
  r["CRAN"] <- "https://mirrors.ustc.edu.cn/CRAN/"
  options(repos = r)
})
```
参考：https://www.r-bloggers.com/permanently-setting-the-cran-repository/
