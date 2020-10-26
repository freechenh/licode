#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: async_demo.py
# @Author: dell
# @Date: 2020/10/26  16:08
# @Desc: 
# @Project: licode
# @Source: PyCharm


import asyncio
import threading


async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()

tasks = [hello(), hello()]

loop.run_until_complete(asyncio.wait(tasks))

loop.close()