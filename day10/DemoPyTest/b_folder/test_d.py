#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: test_d.py
# @Author: dell
# @Date: 2020/6/10  10:40
# @Desc: 
# @Project: bugQuery
# @Source: PyCharm
import pytest

from DemoPyTest.Data import Data


@pytest.mark.usefixtures('demo_fixture')
# @pytest.mark.usefixtures("")
class TestD:

    @pytest.mark.success
    def test_d_1(self):
        assert 2 - 1 == 0

    def test_d_2(self):
        assert 2 - 2 == 0

    @pytest.mark.error
    def test_d_3(self):
        assert 3 + 1 == 3

