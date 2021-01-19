#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: xx.py
# @Author: dell
# @Date: 2021/1/11  13:58
# @Desc: 
# @Project: licode
# @Source: PyCharm
import time

import paramiko

# from paramiko.ssh_exception import

connect_failed_count = 0
connect_success_count = 0


def xx(ip=None):
    global connect_failed_count
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=9622, username='root', password='ruijie')
        return ssh
    except Exception as e:
        connect_failed_count += 1
        print(e)


if __name__ == '__main__':
    for _ in range(5000):
        a = xx('172.28.100.56')
        if a:
            connect_success_count += 1
            chanel_ssh_ob = a.invoke_shell()
            chanel_ssh_ob.send('ls\n\r')
            result = chanel_ssh_ob.recv(9999).decode('utf-8')
        #     stdin, stdout, stderr = a.exec_command("ls")
        #     result = stdout.read()
            print(result)
            chanel_ssh_ob.close()
            a.close()
    print(connect_failed_count)
    print(connect_success_count)
