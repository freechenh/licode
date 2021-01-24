#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: decorator_xxx.py
# @Author: dell
# @Date: 2021/1/5  10:45
# @Desc: 
# @Project: licode
# @Source: PyCharm


def debug(func):
    def wrapper(*args, **kwargs):
        print("[DEBUG]: enter {}()".format(func.__name__))
        func(*args, **kwargs)
        print('xxxxxx')

    return wrapper


@debug
def say_hello(ssss):
    print('hello' + ssss)


# class Test:
#     def __call__(self, *args, **kwargs):
#         print('call me')


if __name__ == '__main__':
    say_hello(ssss='chenhui')
