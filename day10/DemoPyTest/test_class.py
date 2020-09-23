#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: test_class.py
# @Author: dell
# @Date: 2019/12/26
# @Desc: 
# @Project: bugQuery
# @Source: PyCharm
import pytest


class TestClass:

    @pytest.mark.success
    def test_one(self):
        x = 'this'
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")


if __name__ == '__main__':
    pytest.main(['-s', '-v', r'--html=DemoPyTest/report.html'])
