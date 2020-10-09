#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: demo.py
# @Author: dell
# @Date: 2020/9/27  10:25
# @Desc: 
# @Project: licode
# @Source: PyCharm
import requests

url = "https://172.28.100.159:8443/rcdc/rco/admin/getCurrentUserInfo"

login_url = "https://172.28.100.159:8443/rcdc/rco/admin/loginAdmin"

data = {"userName": "admin", "pwd": "$2a$10$oDe3NrglwFsuzfb3VEE4we8XMfQxv1ffTHneEBv84oiUO0kEp01hu",
        "timestamp": 1601175918093}

login_header = {
    "Content-Type": "application/json"
}

header = {
    "Cookie": "JSESSIONID=C2D534DB40ECB6FDE3194ABD3902A7FC; rabbit=true; rcdcuser-status=true",
    "Content-Type": "application/json"
}

# rq_session = requests.session()

# rq_login = rq_session.post(login_url, json=data, headers=login_header, verify=False)

# print(rq_login.headers)
#
# print(rq_login.json())


# login_rq = requests.post(url=login_url, json=data, headers=login_header, verify=False)
#
# print(login_rq.headers)
#
# print(login_rq.json())

rq = requests.post(url, headers=header, verify=False)
print(rq.json())
