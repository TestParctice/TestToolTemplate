# encoding:utf-8
"""
@Software:PyCharm
@Time:2022/12/2 17:02
@Author:yzx
"""
import socket


def get_ip():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return {"Hostname": hostname, "IP_Address": ip_address}


if __name__ == '__main__':
    print(get_ip())
