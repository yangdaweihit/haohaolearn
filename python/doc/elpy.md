# Elpy

[elpy](https://elpy.readthedocs.io/en/latest/index.html) 是Emacs中的
Python开发环境插件。

## 配置

### 软件安装
```
sudo apt install elpa-elpy python3-venv
```

### 基本配置

在`.emacs.d/init.el`或`.custom.el`中插入：
```
(require 'elpy)
(elpy-enable)
(setq elpy-shell-use-project-root nil)
```

## 虚拟环境配置

假设所有虚似环境均在`~/.virtualenv`中，且常用虚拟环境为`myenv`，则设其为
默认激活：

```
(setenv "WORKON_HOME" "~/.virtualenv/")
(pyvenv-activate "~/.virtualenv/myenv")
```

## 交互环境配置

假设已安装`jupyter`：

```
(setq python-shell-interpreter "jupyter"
      python-shell-interpreter-args "console --simple-prompt"
      python-shell-prompt-detect-failure-warning nil)
(add-to-list 'python-shell-completion-native-disabled-interpreters
             "jupyter")
```
    
## 检查配置

- 检查配置： `M-x elpy-config`
- 开启内部python线程：`,-r-p-y`
- 当Eply模式开启时，可以 `C-Enter` 执行当前行语句，并输出到内部Python交
  互界面中

## 快捷键

### Prrojects

- C-u C-c C-c (elpy-shell-send-region-or-buffer)

    Evaluate the current script (or region if something is selected) in
    an interactive python shell. The python shell is automatically
    displayed aside of your script.
    
### Completion

- M-TAB (elpy-company-backend)

    Provide completion suggestions for a completion at point.
    
    You can use cursor keys or M-n and M-p to scroll through the
    options, RET to use the selected completion, or TAB to complete the
    common part.

- C-RET (elpy-shell-send-statement-and-step)

    Evaluate the current statement (current line plus the following
    nested lines). Useful for evaluating a function or class definition
    or a for loop.

- C-c C-z (elpy-shell-switch-to-shell)

    Switch between your script and the interactive shell.

- C-c C-d (elpy-doc)

    Display documentation for the thing under cursor (function or
    module). The documentation will pop in a different buffer, that can
    be closed with q.

- C-c C-s (elpy-rgrep-symbol)

    Search the files in the current project for a string. By default,
    this uses the symbol at point. With a prefix argument, it will
    prompt for a regular expression to search.

### Refactoring

- C-c C-e

    对当前光标所属的符号的同现进行编辑

- C-c C-r f

    用当前格式化工具格式化代码，使用了yapf, autopep8和black。

- C-u C-c C-c

    执行当前脚本

### matplotlib显示图片

- 安装python3-tk
- matplotlib.use('TkAgg')

## 参照

https://elpy.readthedocs.io/en/latest/index.html
