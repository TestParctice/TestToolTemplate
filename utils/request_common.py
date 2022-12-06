# encoding:utf-8
"""
@Software:PyCharm
@Time:2022/12/5 15:58
@Author:yzx
"""
import requests


class Request():
    def __init__(self, url, params, header={}, timeout=30):
        self.url = url
        self.header = header
        self.params = params
        self.timeout = timeout

    def request_by_method(self, method="get", **args):
        if method == "get" or method == "Get" or method == "GET":
            try:
                resp = requests.request(method="GET", url=self.url, headers=self.header, data=self.params,
                                        **args)
                return resp
            except Exception as e:
                return e
        elif method == "post" or method == "Post" or method == "POST":
            try:
                resp = requests.request(method="POST", url=self.url, headers=self.header, data=self.params,
                                        **args)
                return resp
            except Exception as e:
                return e
        elif method == "put" or method == "Put" or method == "PUT":
            try:
                resp = requests.request(method="POST", url=self.url, headers=self.header, data=self.params,
                                        **args)
                return resp
            except Exception as e:
                return e
        elif method == "delete" or method == "Delete" or method == "DELETE":
            try:
                resp = requests.request(method="POST", url=self.url, headers=self.header, data=self.params,
                                        **args)
                return resp
            except Exception as e:
                return e
        else:
            res = str(method) + "暂不支持"
            return res


if __name__ == '__main__':
    resp = Request(url="https://www.bejson.com/Bejson/Api/ShortUrl/getShortUrl",
                   header={
                       "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36"
                   },
                   params={'url': 'http://www.bejson.com'}).request_by_method("post")
    print(resp.json())
