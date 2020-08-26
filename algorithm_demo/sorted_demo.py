#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: sorted_demo.py
# @Author: dell
# @Date: 2020/8/25  17:20
# @Desc: 
# @Project: licode
# @Source: PyCharm


def xxx(nums):
    for i in range(len(nums)):
        count = len(nums) - 1
        for j in range(count):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
        count -= 1
        print(nums)
    return nums


def find_smallest(nums):
    smallest = nums[0]
    smallest_index = 0
    for i in range(1, len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
            smallest_index = i
    return smallest_index


def select_sort(nums):
    new_nums = []
    for i in range(len(nums)):
        smallest = find_smallest(nums)
        new_nums.append(nums.pop(smallest))
    return new_nums


print(select_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))


# print(xxx([9, 8, 7, 6, 5, 4, 3, 2, 1]))
