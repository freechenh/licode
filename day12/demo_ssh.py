#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: demo_ssh.py
# @Author: dell
# @Date: 2020/10/9  15:28
# @Desc: 
# @Project: licode
# @Source: PyCharm


import paramiko

transport = paramiko.Transport(('172.28.100.59', 9622))
transport.connect(username='root', password='ruijie')
ssh = paramiko.SSHClient()
ssh._transport = transport


def xxx():
    stdin, stdout, stderr = ssh.exec_command('ls')
    print(stdout.read().decode("utf-8"))

    stdin, stdout, stderr = ssh.exec_command('ls')
    print(stdout.read().decode("utf-8"))


for _ in range(1000):
    xxx()

transport.close()
