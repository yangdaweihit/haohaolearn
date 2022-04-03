import os
import subprocess

# os 杂项操作系统界面
# https://docs.python.org/2/library/os.html
# open() : 读写文件
# os.path : 操作路径
# fileinput : 读取所有文件中的所有行
# tempfile : 生成临成文件和文件夹

if __name__ == '__main__':

    # os.chdir(path)
    # Change the current working directory to path.
    os.chdir("/home/wall-e")
    subprocess.call("ls")

    # os.getcwd()
    # Return a string representing the current working directory.
    print("当前工作目录为 : %s" % os.getcwd())

    # os.open()
    # 打开一个文件或文件夹，并且设置需要的打开选项，模式参数mode参数是可选的，默
    # 认为 0777。
    fd = os.open("/home/wall-e/", os.O_RDONLY)

    # Change the current working directory to the directory represented by the
    # file descriptor fd. The descriptor must refer to an opened directory,
    # not an open file.
    os.fchdir(fd)
    print("当前工作目录为 : %s" % os.getcwd())

    # 15.1.4 文件和文件夹

    # os.access(path, mode) Using access() to checkif a user is
    # authorized to e.g. open a file before actually doing so using
    # open() creates a security hole, because the user might exploit the
    # short time interval between checking and opening the file to
    # manipulate it.

    if os.access("/home/wall-e/.zshrc", os.R_OK):
        with open("/home/wall-e/.zshrc") as fp:
            print(fp.read())

    # os.path.dirname
