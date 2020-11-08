#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: pool_demo.py
# @Author: dell
# @Date: 2020/10/26  17:26
# @Desc: 
# @Project: licode
# @Source: PyCharm


from multiprocessing import Pool

import os, time, random


def task_long_time(name):
    print("run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print("task %s runs %0.2f seconds" % (name, (end - start)))
    pass


if __name__ == '__main__':
    print("parent process %s." % os.getpid())
    p = Pool(9)
    for i in range(10):
        p.apply_async(task_long_time, args=(i,))
    print("waiting for all subprocess done")
    p.close()
    p.join()
    print("all subprocess done")
