#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: test_a.py
# @Author: dell
# @Date: 2020/6/10  10:38
# @Desc: 
# @Project: bugQuery
# @Source: PyCharm


import pytest


@pytest.fixture()
def xx():
    print("前置条件")
    yield 1, 2
    print("收尾条件")


data = [1, 2, 3, 4, 5, 6]


class TestA:

    @pytest.mark.parametrize("data_", data)
    def test_a_1(self, data_):
        assert data_ > 3

    def test_a_2(self):
        a, b = xx
        assert a + b == 3
