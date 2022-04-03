;; Happy hacking wall-e - Emacs loves you!

(+ 2 (+ 3 3))
(fill-column)
(+ 2  2)
(concat "abc" "def")
;;; set
(set 'flowers '(rose violet daisy buttercup))
;;; setq
(setq nlowers '(rose violet daisy buttercup))

'flowers

(buffer-name)
(buffer-file-name)
(current-buffer)
(other-buffer)
(buffer-size)
(point)

(defun myfun (x y)
  "my first function"
  (interactive)
  ;; (message "hello, emacs.")
  (+ (* x x) (* y y)))

(myfun 3 4)
