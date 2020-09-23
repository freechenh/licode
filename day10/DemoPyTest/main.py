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
    pytest.main(["--alluredir", "./report"])
    # pytest.main(["-q"], ["test_class.py::TestClass::test_one"])
