#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: example_demo.py
# @Author: dell
# @Date: 2020/9/7  11:34
# @Desc: 
# @Project: licode
# @Source: PyCharm


class Solution:

    def __init__(self):
        self.name = "your name is :"
        self.age = None

    def set_name(self, name):
        print(self.name + name)


if __name__ == '__main__':
    demo = Solution()
    demo.set_name("chenhui")
    demo.set_name("lijuan")
