#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: algorithm.py
# @Author: dell
# @Date: 2020/8/25  16:17
# @Desc: 
# @Project: licode
# @Source: PyCharm


def binary_search(list_, item_):
    """
    二分法
    :param list_:
    :param item_:
    :return:
    """
    low = 0
    high = len(list_) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list_[mid]
        if guess == item_:
            return mid
        if guess > item_:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))
print(binary_search(my_list, -1))

"""
128 > 64 > 32 > 16 > 8 > 4 > 2 > 1
"""
