# encoding:utf-8
"""
@Software:PyCharm
@Time:2022/12/5 16:38
@Author:yzx
"""
import hashlib


def md5_key(arg):
    md5 = hashlib.md5()
    md5.update(arg.encode("utf8"))
    return md5.hexdigest()


if __name__ == '__main__':
    print(md5_key("yzx"))
