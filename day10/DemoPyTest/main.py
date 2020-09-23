#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: main.py
# @Author: dell
# @Date: 2020/6/10  11:17
# @Desc: 
# @Project: bugQuery
# @Source: PyCharm

import pytest


if __name__ == '__main__':
    # pytest.main(["--alluredir", "./report"])
    # pytest.main(["-x", "test_class.py"])
    pytest.main(['-q', 'a_folder/', "--alluredir", "./report"])
    pytest.main(['-q', 'b_folder/', "--alluredir", "./report"])
