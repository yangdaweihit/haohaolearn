# Visual Studio Code

[vscode](https://code.visualstudio.com/)是一款轻量且强大的源
码编辑器，vscode有丰富的LaTeX插件，便于编辑编译tex文档。

## 主要插件

- LaTeX Workshop

## 配置文件

`Ctrl+Shift+p`：Open Settings (JSON)

输入配置文件：

```
{
    "latex-snippets.autoSuggestionOn": true,
    "latex-workshop.view.pdf.viewer": "tab",
    "latex-workshop.latex.tools": [
      {
          "name": "xelatex",
          "command": "xelatex",
          "args": [
              "-synctex=1",
              "-interaction=nonstopmode",
              "-file-line-error",
              "-pdf",
              "%DOC%"
          ]
      },
      {
          "name": "latexmk",
          "command": "latexmk",
          "args": [
              "-synctex=1",
              "-interaction=nonstopmode",
              "-file-line-error",
              "-pdf",
              "%DOC%"
          ]
      },
      {
          "name": "pdflatex",
          "command": "pdflatex",
          "args": [
              "-synctex=1",
              "-interaction=nonstopmode",
              "-file-line-error",
              "%DOC%"
          ]
      },
      {
          "name": "bibtex",
          "command": "bibtex",
          "args": [
              "%DOCFILE%"
          ]
      }
  ],
  "latex-workshop.latex.recipes": [
      {
          "name": "xelatex",
          "tools": [
              "xelatex"
          ]
      },
      {
          "name": "pdflatex -> bibtex -> pdflatex*2",
          "tools": [
              "pdflatex",
              "bibtex",
              "pdflatex",
              "pdflatex"
          ]
      }
  ]
}
```


## 快捷键

- `Ctrl + Alt + B`: 编译