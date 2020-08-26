#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: factorial_demo.py
# @Author: dell
# @Date: 2020/8/25  18:19
# @Desc: 
# @Project: licode
# @Source: PyCharm


def fact(x):
    if x == 1:
        return x
    x = x * fact(x - 1)
    return x


# print(fact(5))

def sum_demo(nums):
    if len(nums) == 1:
        return nums[0]
    return nums[0] + sum_demo(nums[1:])


def sum_count(nums):
    if len(nums) == 1:
        return 1
    return 1 + sum_count(nums[1:])


def sum_max(nums):
    if len(nums) == 2:
        return nums[1] if nums[0] < nums[1] else nums[0]
    if nums[0] > nums[1]:
        nums[0], nums[1] = nums[1], nums[0]
    return sum_max(nums[1:])


def nums_sort(nums):
    pass


def quick_sort(nums):
    if len(nums) < 2:
        return nums
    else:
        pivot = nums[0]
        less = [i for i in nums[1:] if i <= pivot]
        greater = [i for i in nums[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([5, 4, 3, 2, 1]))
