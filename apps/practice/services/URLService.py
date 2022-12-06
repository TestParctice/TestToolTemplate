# encoding:utf-8
"""
@Software:PyCharm
@Time:2022/12/5 15:54
@Author:yzx
"""
from practice.models import URLInfo
from utils import ip


class URLService:
    def __init__(self):
        self.api_info = URLInfo()

    def save_url_info(self, longUrl, smallUrl, ipMsg, remark=""):
        self.api_info.longUrl = longUrl
        self.api_info.smallUrl = smallUrl
        self.api_info.ipMsg = ip.get_ip()
        self.api_info.remark = remark
        try:
            print(self.api_info)
            self.api_info.save()
            return True
        except Exception as e:
            return e


if __name__ == '__main__':
    pass
