#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: ssh_demo.py
# @Author: dell
# @Date: 2020/9/2  16:02
# @Desc: 
# @Project: licode
# @Source: PyCharm


# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File: xshell.py
# @Author: dell
# @Date: 2020/4/13  11:42
# @Desc:
# @Project: bugQuery
# @Source: PyCharm
import re
import time

import paramiko


class Demo:

    def __init__(self):
        self._transport = None
        self._channel = None

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

    def send(self, cmd):
        cmd += "\n"
        p = re.compile(r'\[root.*?\]#')
        result = ''
        self._channel.send(cmd)
        self._channel.settimeout(20)
        while True:
            ret = self._channel.recv(65535)
            ret = ret.decode("utf-8")
            result += ret
            if len(p.findall(result)) == 2:
                break
        print(result)

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
    # transport.send('cd /home', channel)
    # transport.send('rm -f or.sh', channel)
    # transport.send('ls -l', channel)
    # input_pwd = "Are you sure you want to continue connecting (yes/no)?"

    # cmd_write = "dd if=/dev/urandom of=/home/gejian/test2.log bs=1M count=1000"

    # cmd_cksum = "cksum /home/gejian/test2.log | awk '{print $1}"

    cmd = "cd vdbench"

    cmd_1 = "ls"

    transport.send(cmd)
    transport.send(cmd_1)
    # tmp1 = transport.send_middle("/opt/java/zookeeper/bin/zkCli.sh", channel)
    # if "zk: localhost:2181(CONNECTED)" in tmp1:
    #     tmp2 = transport.send_middle("get /pos/cluster/nodes/1", channel)

    transport.transport_disconnect()
