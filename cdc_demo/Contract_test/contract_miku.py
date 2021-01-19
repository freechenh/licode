#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: contract_miku.py
# @Author: dell
# @Date: 2021/1/18  16:02
# @Desc: 
# @Project: licode
# @Source: PyCharm
import atexit
import unittest
from pact import Consumer, Provider

# 构造pact对象，定义消费者服务的名字并给它一个生产者服务
from cdc_demo.Contract_test.query import get_cartoon_characters

pact = Consumer('Consumer Miku').has_pact_with(Provider('Provider'))
pact.start_service()
# 注册退出的时候关闭pact服务
atexit.register(pact.stop_service)


class GetMikuInfoContract(unittest.TestCase):

    def test_miku(self):
        # 定义响应期望的结果
        expected = {
            "salary": 45000,
            "name": "Hatsune Miku",
            "nationality": "Japan",
            "contact": {
                "Email": "hatsune.miku@woniuxy.com",
                "Phone Number": "13900110001"
            }
        }
        # 定义响应头
        headers = {
            "Content-Type": "application/json"
        }
        # 定义模拟生产者提供者接受请求以及响应的方式
        (pact
         .upon_receiving('a request for Miku')
         .with_request(
            method='GET',
            path='/information',
            query={'name': 'miku'}
        ).will_respond_with(200, headers, expected))
        # 定义消费者服务向模拟生产者发出请求并活得响应
        with pact:
            result = get_cartoon_characters('miku')
        # 做最后的断言
        self.assertEqual(result.json(), expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)
