 读取summary.csv数据转换为tex表格格式，写入到summary.tex
# M-; 注释
# C-u C-c C-c 执行脚本
# C-c C-r f elpy-format-code
# C-c C-v 检查代码

import re
outfile = open('summary.tex', 'w')

with open('summary.csv', 'r') as infile:
    for line in infile:
        line.rstrip('\n')
        line = re.sub(',', ' & ', line) + r'\\'  # + '\n'
        outfile.write(line)

infile.close()
outfile.close()
