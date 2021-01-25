#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: ddd.py
# @Author: dell
# @Date: 2021/1/20  18:41
# @Desc: 
# @Project: licode
# @Source: PyCharm


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        more = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(more)


if __name__ == '__main__':
    print(quick_sort([10, 5, 2, 3]))
