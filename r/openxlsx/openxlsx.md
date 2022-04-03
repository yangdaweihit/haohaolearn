# openxlsx

## 描述

提供了一个高级界面生成Excel表格(.xlsx)，简化了写入、风格化、和编辑表格(worksheets)的操作。功能可与`xlsx`和`XLConnect`比美磁，且移除了对Java的依赖。

## 维护者

Alexander Walker 

## 文档

- [openxlsx](https://mran.microsoft.com/web/packages/openxlsx/openxlsx.pdf)

## 要点

### 加载表格

- `loadWorkbook`: 返回一个WorkBook对象，包括`.xlsx`文件的风格和格式。
- `readWorkbook`：从Excel文件中或WorkBook对象中读取数据，存入data.frame。

```
# 从openxlsx包中加载loadExample.xlsx文件，返回对象wb
wb <- loadWorkbook(file = system.file("loadExample.xlsx", package= "openxlsx"))
# 列出表单名
names(wb) 
# 在wb中增加一个表单，名为 A new worksheet
addWorksheet(wb, "A new worksheet")
# 保存数据表对象到文件中
saveWorkbook(wb, "loadExample.xlsx", overwrite = TRUE)

wb <- loadWorkbook("data.xlsx")
df <- readWorkbook(xlsxFile = wb,sheet=1,rowNames=FALSE)
```
