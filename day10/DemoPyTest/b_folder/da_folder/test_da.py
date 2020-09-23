#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: test_da.py
# @Author: dell
# @Date: 2020/6/10  10:35
# @Desc: 
# @Project: bugQuery
# @Source: PyCharm
import pytest


@pytest.mark.error
class TestDa:

    def test_a(self):
        assert 1 + 1 == 2

    @pytest.mark.db
    def test_b(self):
        assert 1 + 1 == 3
