import inspect
import os

# 获取当前脚本所在文件夹
fpath = os.path.dirname(inspect.getfile(lambda: None))
print(fpath)
os.chdir(fpath)