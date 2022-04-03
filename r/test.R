#  http://iltabiai.github.io/tips/latex/2015/09/15/latex-tikzdevice-r.html
# tikz("tikz-example.tex",width = 3.25, height = 3.25)
# print(plot(1, 1, main = "Hello \\TeX !"))
# dev.off()
library(tikzDevice)
options(tikzMetricPackages = c("\\usepackage[utf8]{inputenc}",
    "\\usepackage[T1]{fontenc}", "\\usetikzlibrary{calc}",
    "\\usepackage{amssymb}"))
## I need the amssymb package because I use \mathcal and \mathbb
tikz("formula.tex", width = 4, height = 4, standAlone = TRUE,
    packages = c("\\usepackage{tikz}",
                 "\\usepackage[active,tightpage,psfixbb]{preview}",
                 "\\PreviewEnvironment{pgfpicture}",
                 "\\setlength\\PreviewBorder{0pt}",
                 "\\usepackage{amssymb}"))
par(mar = c(4, 4,2,2), mgp = c(2, 0.9, 0))
plot(1, type = "n", xlab = "$\\alpha_1$", ylab = "$\\xi$",main="\\LaTeX{}")
text(1, c(0.8, 1, 1.2), c("$\\underbrace{1,2,\\cdots,10}_{10}$",
    "$\\mathbb{ABCDEFG}$", "$\\mathcal{HIJKLMN}$"), cex = 2.5)
dev.off()

tools::texi2pdf("formula.tex")
system(paste(getOption("pdfviewer"), "formula.pdf"))