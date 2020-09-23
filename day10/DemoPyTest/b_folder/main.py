#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: main.py
# @Author: dell
# @Date: 2020/6/10  11:19
# @Desc: 
# @Project: bugQuery
# @Source: PyCharm

import pytest


if __name__ == '__main__':
    pytest.main(["-m", "not error and not success"])
