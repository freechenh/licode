#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: xxx.py
# @Author: dell
# @Date: 2021/1/11  11:31
# @Desc: 
# @Project: licode
# @Source: PyCharm


class Xxx:
    def __init__(self):
        self.aa = 1
        self.bb = 2

    def a(self):
        print("self.aa的值是 %s" % self.aa)
        return 1

    def ab(self):
        demo = self.a()
        if demo:
            cc = demo
            print(cc)


if __name__ == '__main__':
    a = Xxx()
    a.ab()
