#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: increase_iterable.py
# @Author: dell
# @Date: 2020/8/25  14:42
# @Desc: 
# @Project: licode
# @Source: PyCharm


class Solution:
    @staticmethod
    def find_sub_sequences(nums):
        result = list()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                demo = list()
                demo.append(nums[i])
                demo.append(nums[j])
                if demo not in result:
                    result.append(demo)
        return result


print(Solution().find_sub_sequences([4, 6, 7, 7]))
