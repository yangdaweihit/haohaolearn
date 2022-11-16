#! /usr/bin/python3
# -*- coding: utf-8 -*-

import json
import subprocess
import time
if __name__ == '__main__':

    start_time = time.time()
    subprocess.call("xelatex mytest.tex", shell=True)
    print("--- %s seconds ---" % (time.time() - start_time))
