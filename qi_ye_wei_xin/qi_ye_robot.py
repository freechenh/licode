#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: qi_ye_robot.py
# @Author: dell
# @Date: 2020/12/1  10:36
# @Desc: 
# @Project: licode
# @Source: PyCharm


import requests
from threading import Timer
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


# url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=3e8e010c-a0a5-4400-87a9-8525c14df72c"


def print_time(inc):
    print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    t = Timer(inc, print_time, (inc,))
    t.start()


print_time(5)
