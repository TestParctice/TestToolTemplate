# encoding:utf-8
"""
@Software:PyCharm
@Time:2022/12/3 13:45
@Author:yzx
"""

# from apps.practice.models import APIInfo
from practice.models import APIInfo
from utils import ip

"""
这样引用的原因：不这样引用的话，会报错:
RuntimeError: Model class apps.practice.models.APIInfo doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS.
原因:整合了多个app，将他们放到一个文件夹apps下，但是在django的setting配置中，
    已经将apps的路径配置sys.path.insert(0, os.path.join(BASE_DIR, "apps"))
"""


class APIService:
    def __init__(self):
        self.api_info = APIInfo()

    def save_api_info(self, url, params, responseDaa, apiType, header, apiParamsType):
        self.api_info.url = url
        self.api_info.responseDaa = responseDaa
        self.api_info.apiParams = params
        self.api_info.apiType = apiType
        self.api_info.header = header
        self.api_info.apiParamsType = apiParamsType
        self.api_info.remark = ip.get_ip()
        try:
            print(self.api_info)
            self.api_info.save()
            return True
        except Exception as e:
            return e


if __name__ == '__main__':
    import os

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TestToolsSetting.settings.settings')
    res = APIService().save_api_info(url="http://www.baiodu.com", params={"param": "1123"},
                                     responseDaa={"responseDaa": "responseDaa"}, apiType="get",
                                     header={"header": "header"},
                                     apiParamsType="jsonp")
    print(res)

# django.core.exceptions.ImproperlyConfigured: Requested setting INSTALLED_APPS, but settings are not configured.
# You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
