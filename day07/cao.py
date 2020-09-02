#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: cao.py
# @Author: dell
# @Date: 2020/9/2  17:07
# @Desc: 
# @Project: licode
# @Source: PyCharm

import re
import time

import paramiko


class Demo:

    def __init__(self):
        self._transport = None
        self._channel = None
        self._count = 0

    def transport_connect(self, info):
        self._transport = paramiko.Transport((info[0], info[1]))
        self._transport.start_client()
        self._transport.auth_password(info[2], info[3])

        self._channel = self._transport.open_session()
        self._channel.get_pty()

        self._channel.invoke_shell()

        return self._transport, self._channel

    def transport_disconnect(self):
        if self._channel:
            self._channel.close()
        if self._transport:
            self._transport.close()

    def send(self, cmd, channel, max_time=100):
        # command = cmd
        self._count += 1
        cmd += "\r"
        p = re.compile(r'\[root.*?\]#')
        result = ''
        self._channel.send(cmd)
        # self._channel.settimeout(max_time)
        while max_time > 0:
            time.sleep(0.2)
            ret = self._channel.recv(65535)
            ret = ret.decode("utf-8")
            result += ret
            print(ret)
            if len(p.findall(result)) == 2 and self._count == 1:
                break
            if len(p.findall(result)) == 1 and self._count > 1:
                break
            max_time -= 1
        return result

    @staticmethod
    def send_middle(cmd, channel):
        cmd += "\n"
        channel.send(cmd)
        time.sleep(0.5)
        ret = channel.recv(65535)
        ret = ret.decode('utf-8')
        print("%s cmd output is : " % cmd + ret)
        return ret


if __name__ == '__main__':
    ip_info = ['172.28.37.110', 9622, 'root', "ruijie"]
    transport = Demo()
    channel = transport.transport_connect(ip_info)[1]
    transport.send('cd vdbench', channel)
    transport.send('ls -l', channel)

    cmd_write = "dd if=/dev/urandom of=/home/gejian/test2.log bs=1M count=1000"

    cmd_cksum = "cksum /home/gejian/test2.log | awk '{print $1}'"

    transport.send(cmd_write, channel)
    transport.send(cmd_cksum, channel)
    # input_pwd = "Are you sure you want to continue connecting (yes/no)?"
    #
    # tmp1 = transport.send_middle("/opt/java/zookeeper/bin/zkCli.sh", channel)
    # if "zk: localhost:2181(CONNECTING)" in tmp1:
    #     tmp2 = transport.send_middle("get /pos/cluster/nodes/1", channel)

    transport.transport_disconnect()
