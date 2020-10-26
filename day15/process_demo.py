#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: process_demo.py
# @Author: dell
# @Date: 2020/10/26  15:50
# @Desc: 
# @Project: licode
# @Source: PyCharm

import multiprocessing
import time


def process_run(n):
    time.sleep(1)
    print("process", n)


def multiprocess_demo():
    for i in range(10):
        p = multiprocessing.Process(target=process_run, args=(i,))
        p.start()
        # p.join()


if __name__ == '__main__':
    multiprocess_demo()
