#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: asyncio_demo.py
# @Author: dell
# @Date: 2020/10/26  16:00
# @Desc: 
# @Project: licode
# @Source: PyCharm


import asyncio
import threading

from day15.process_demo import multiprocess_demo


@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    multiprocess_demo()
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()

tasks = [hello(), hello()]

loop.run_until_complete(asyncio.wait(tasks))

loop.close()
