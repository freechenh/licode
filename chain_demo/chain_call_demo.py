#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: chain_call_demo.py
# @Author: dell
# @Date: 2021/1/19  10:44
# @Desc: 
# @Project: licode
# @Source: PyCharm


class Person:

    # def __init__(self):
    #     self.name = None
    #     self.age = None

    def name(self, name):
        self.name = name
        return self

    def age(self, age):
        self.age = age
        return self

    def show(self):
        print(self.name, self.age)


if __name__ == '__main__':
    p = Person()
    (p
     .name('tyh')
     .age(15)
     .show())
