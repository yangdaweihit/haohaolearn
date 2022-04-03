# Beamer

## 选项

| 选项        | 描述 | 示例            |
|-------------|------|-----------------|
| aspectratio | 比例 | aspectratio=169 |

## 校徽

用于授课和学术会议的幻灯片经常需要使用校徽。中国各知名大学的校徽可以通过
[cnlogo](https://github.com/yuxtech/cnlogo)制作。

```
\documentclass{article}
% \documentclass{standalone}
\usepackage[hiu]{cnlogo}
\usepackage{graphicx}

\definecolor{HITBlue}{rgb}{0, 0.48 ,0.65} %#007BA7

\begin{document}

% \hiuwhole[coreBlue][0.2]

\hiutext[HITBlue][4]
\vskip2em
\hiulogo[HITBlue][4]
\vskip2em
\hiuwhole[HITBlue][4]

\end{document}
```

## 显示注释

```
\usepackage{pgfpages}
\setbeameroption{show notes on second screen}
```

使用[impressive](http://impressive.sourceforge.net/)


## 参考

- [impressive](https://github.com/geekq/impressive)