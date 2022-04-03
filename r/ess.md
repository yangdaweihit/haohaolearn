# ESS

[ESS](https://ess.r-project.org/)是GNU Emacs的插件，支持各种统计分析程序
如R、S-Plus、SAS、Sdata和OpenBUGS/JAGS等脚本编辑和交互，详见见[文
档](https://ess.r-project.org/ess.pdf)。

# 配置

```
(require 'ess-site)
(setq tramp-ssh-controlmaster-options nil) ;;解决启动卡死的问题。这个是关于TRAMP的bug，解决方案来自于<https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=810640>。dsfadfsdaf
(eval-after-load "comint"
  '(progn
      (define-key comint-mode-map [up]
        'comint-previous-matching-input-from-input)
      (define-key comint-mode-map [down]
        'comint-next-matching-input-from-input)
      ;; also recommended for ESS use --
      (setq comint-scroll-to-bottom-on-output 'others)
      (setq comint-scroll-show-maximum-output t)
      ;; somewhat extreme, almost disabling writing in *R*, *shell* buffers above promp
      (setq comint-scroll-to-bottom-on-input 'this)
))
```

## 启动 

`M-x R RET`

弹出一个名为`*R`的缓冲窗，用于R交互。

## 交互

| 快捷键  | 函数                                              | 描述                  |
|---------|---------------------------------------------------|-----------------------|
| M-;     |                                                   | 注释                  |
| C-c C-l | ess-load-file filename                            | 将文件加载到ESS进程中 |
| C-c C-b | ess-eval-buffer                                   |                       |
| C-c C-c | ess-eval-region-or-function-or-paragraph-and-step |                       |
| C-c C-f | ess-eval-function                                 |                       |
| C-c C-j | ess-eval-line                                     |                       |
| C-c C-r | ess-eval-region                                   |                       |
| C-c C-q | ess-eval-quit                                     |                       |

# 调试

  - 设置断点(C-c C-t b)后，加载文件(C-c C-l)
  - 在开启的Browser中，用`n`或`c`或`f`控制执行
  - 打开观察窗口(C-c C-t w)，填加观察变量
  - 在Browser中，按`Q`退出，或按`f`执行并退出。
