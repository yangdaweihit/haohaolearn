(menu-bar-mode -1) ;;关闭菜单
(scroll-bar-mode -1) ;; 关闭滚动条
(global-hl-line-mode 1)
(setq  initial-frame-alist (quote ((fullscreen . maximized))))
(setq make-backup-files nil) ;; disable auto backup files
(define-key global-map (kbd "C-x e") 'multi-term)

;; (run-with-idle-timer 0.1 nil 'toggle-fullscreen)

(defun open-my-init-file()
  (interactive)
  (find-file "~/.custom.el")
  )

(global-set-key (kbd "<f2>") 'open-my-init-file)

(unless (eq 'org-mode major-mode)
   (setq-default fill-column 72))

(setq-default truncate-lines t) ;; which is default
(setq truncate-partial-width-windows t)
(setq-default auto-fill-function 'do-auto-fill)
;; (setq tramp-ssh-controlmaster-options nil)
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 ;; '(initial-frame-alist (quote ((fullscreen . maximized))))
;; '(markdown-command "pandoc -f markdown -t html -s --mathjax --highlight-style pygments")
;;)

;; ansys-mode

(autoload 'ansys-mode "ansys-mode" "Activate ANSYS-Mode." 'interactive)

(add-to-list 'auto-mode-alist '("\\.mac$" . ansys-mode))
(add-to-list 'auto-mode-alist '("\\.dat$" . ansys-mode))
(add-to-list 'auto-mode-alist '("\\.inp$" . ansys-mode))
;; this is the suffix for "ANSYS Neutral Files" which include some APDL.
(add-to-list 'auto-mode-alist '("\\.anf$" . ansys-mode))

(defun turn-on-outline-minor-mode ()
(outline-minor-mode 1))

(add-hook 'LaTeX-mode-hook 'turn-on-outline-minor-mode)
(add-hook 'latex-mode-hook 'turn-on-outline-minor-mode)
(setq outline-minor-mode-prefix "\C-c \C-o") ; Or something else

(add-to-list 'custom-theme-load-path "~/.emacs.d")
(load-theme 'dracula t)

(require 'cdlatex)
(add-hook 'LaTeX-mode-hook 'turn-on-cdlatex)

(require 'cnfonts)
(cnfonts-enable)

;; (require 'ess-site)
;; (add-hook 'ess-post-run-hook 'ess-tracebug)
;; (require 'ess-smart-underscore)
;; (setq eim-wb-use-gbk t)

;; ================
;; Auctex
;; ================
(add-to-list 'auto-mode-alist '("\\.tex$" . latex-mode))
(require 'tex)
(setq TeX-auto-save t)
(setq TeX-parse-self t)
(setq-default TeX-master nil)

(mapc (lambda (mode)
(add-hook 'latex-mode-hook mode))
      (list 'auto-complete-mode
   'auto-fill-mode
   'LaTeX-math-mode
   'turn-on-reftex
   'linum-mode))
(add-hook 'latex-mode-hook
          (lambda ()
            (setq TeX-auto-untabify t     ; remove all tabs before saving
                  TeX-engine 'xetex       ; use xelatex default
                  TeX-show-compilation t) ; display compilation windows
            (TeX-global-PDF-mode t)       ; PDF mode enable, not plain
            (setq TeX-save-query nil)
            (imenu-add-menubar-index)
            (define-key LaTeX-mode-map (kbd "TAB") 'TeX-complete-symbol)))

 ;; set pdf view tool
 (setq TeX-view-program-list '(("Evince" "evince %o")))
 (cond
  ((eq system-type 'windows-nt)
   (add-hook 'LaTeX-mode-hook
             (lambda ()
               (setq TeX-view-program-selection '((output-pdf "SumatraPDF")
                                                  (output-dvi "Yap"))))))
  ((eq system-type 'gnu/linux)
   (add-hook 'LaTeX-mode-hook
             (lambda ()
               (setq TeX-view-program-selection '((output-pdf "Evince")
                                                  (output-dvi "Evince")))))))
 ; XeLaTeX
 (add-hook 'LaTeX-mode-hook (lambda()
     (add-to-list 'TeX-command-list '("XeLaTeX" "%`xelatex%(mode)%' %t" TeX-run-TeX nil t))
     (setq TeX-command-default "XeLaTeX")
     (setq TeX-save-query  nil )
     (setq TeX-show-compilation t)
     ))

(autoload 'reftex-mode "reftex" "RefTeX Minor Mode" t)
(autoload 'turn-on-reftex "reftex" "RefTeX Minor Mode" nil)
(autoload 'reftex-citation "reftex-cite" "Make citation" nil)
(autoload 'reftex-index-phrase-mode "reftex-index" "Phrase Mode" t)
(add-hook 'latex-mode-hook 'turn-on-reftex) ; with Emacs latex mode
(add-hook 'reftex-load-hook 'imenu-add-menubar-index)
(add-hook 'LaTeX-mode-hook 'turn-on-reftex)

(setq LaTeX-eqnarray-label "eq"
      LaTeX-equation-label "eq"
      LaTeX-figure-label "fig"
      LaTeX-table-label "tab"
      LaTeX-myChapter-label "chap"
      TeX-auto-save t
      TeX-newline-function 'reindent-then-newline-and-indent
      TeX-parse-self t
      TeX-style-path
      '("style/" "auto/"
        "/usr/share/emacs21/site-lisp/auctex/style/"
        "/var/lib/auctex/emacs21/"
        "/usr/local/share/emacs/site-lisp/auctex/style/")
      LaTeX-section-hook
      '(LaTeX-section-heading
        LaTeX-section-title
        LaTeX-section-toc
        LaTeX-section-section
        LaTeX-section-label)
      )

(require 'pyvenv)
(pyvenv-workon "myenv")

(require 'elpy)
(elpy-enable)