# 安装
   
## 命令

   - python -m pip install jupyter

## Emacs配置

[Jupyter console](https://jupyter-console.readthedocs.io/en/stable/)使用Jupyter协议的前端。为在Elpy中默认采用其作为终端，配
置如下：

```
(setq python-shell-interpreter "jupyter"
      python-shell-interpreter-args "console --simple-prompt"
      python-shell-prompt-detect-failure-warning nil)
(add-to-list 'python-shell-completion-native-disabled-interpreters
             "jupyter")

```

-- [Jupyter Notebook](https://jupyter.readthedocs.io/en/latest/running.html)

Jupyter Notebook是Jupyter的web端界面。

- 启动
```
jupyter notebook
```

# 使用

| 快捷键 | 功能         |
|--------|--------------|
| h      | 弹出帮助菜单 |


## Cell状态

| 状态                   | 特征                           | 快捷键                     |
|------------------------|--------------------------------|----------------------------|
| 命令状态(Command Mode) | 蓝色边条， 右上角有一个空图标  | Enter 从命令模式到编辑模式 |
| 编辑状态(Edit Mode)    | 绿色边条，右上角有一个笔状图标 | Esc 回到命令状态           |

## Cell类型切换

| 快捷键 | 功能     |
|--------|----------|
| y      | Code     |
| m      | markdown |


## 移动

| 快捷键 | 功能         |
|--------|--------------|
| j      | 向下移动一行 |
| k      | 向上移动一行 |

## 快捷键

| 快捷键  | 功能                                             |
|---------|--------------------------------------------------|
| S-Enter | 执行当前代码块或渲染Markdown并跳到下一个代码块   |
| C-Enter | 执行当前代码块或渲染Markdown，并不跳转           |
| M-Enter | 执行当前代码块或渲染Markdown，并在下方新建代码块 |
| B1+m    | 变为Markdown单元格                               |
| B1+y    | 变代代码单元格                                   |
| B1+a    | 在上方创建代码块                                 |
| B1+b    | 在下方创建代码块                                 |
| B1+dd   | 删除当前行                                       |
| c       | 复制代码块                                       |
| S-v     | 粘帖代码块                                       |
| Esc z   | 撤销上一个动作                                   |

# 参考

- [python数据分析神器Jupyter notebook快速入门](https://www.bilibili.com/video/av54100790?from=search&seid=13376866229910152959)