#! /usr/bin/python3
# -*- coding: utf-8 -*-

# ansys脚本调用示例
# python3 callansys.py vm1.dat
# subprocess文档：https://docs.python.org/2/library/subprocess.html


import subprocess
import sys
import os.path
import argparse


def ansys_batch(datfile):

    if os.path.exists(datfile) == 0:
        sys.exit("the file not existed!")
    else:
        print(
            "The script {0} has been running, please wait ...".format(datfile))

    prename, ext = os.path.splitext(datfile)

    cmd = ["ansys190", "-b < {0} > {1}.out".format(datfile, prename)]
    res = subprocess.check_call(cmd)
    if res != 0:
        sys.exit("ansys script failed!")
    else:
        print("Successfully Done!")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("datfile", help="input commands file ")
    args = parser.parse_args()  # returns data from the options specified

    # 批处理执行脚本
    ansys_batch(args.datfile)
