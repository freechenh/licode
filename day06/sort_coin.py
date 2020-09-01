#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: sort_coin.py
# @Author: dell
# @Date: 2020/9/1  17:26
# @Desc: 
# @Project: licode
# @Source: PyCharm


class Solution:

    @staticmethod
    def arrange_coin(n):
        start = 0
        end = n
        while start <= end:
            index = (end + start) // 2
            data = int((1 + index) / 2 * index)
            if data == n:
                return index
            if data > n:
                end = index - 1
            else:
                start = index + 1
        return end


if __name__ == '__main__':
    demo = Solution()
    print(demo.arrange_coin(8))
