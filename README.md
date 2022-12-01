# TestToolTemplate
基于Django的测试工具模板
测试工具 Django版本：Django:3.2.13 使用时需要在TestTools下增加config文件，用来保存数据库信息， 例如： config.py: mysql_message = {'ENGINE': 'django.db.backends.mysql', 'NAME': '', 'USER': '', 'PASSWORD': '', 'HOST': '', 'PORT': '***'} 

# 目录结构
>README.md 介绍目录结构，使用说明

>apps
>>各业务自己创建的应用，目前没有严格的规范，合理即可

>TestToolsSettings
>>settings配置文件所在位置
>>>dbc:封装的数据库连接方法
>>>settings:django的settings配置文件
>>>urls.py 整体的urls路径地址

>static
>>整体的静态文件存放地址，跟apps内的应用对应，每个模块都有自己的static文件

>templates
>>html文件存放地址，跟apps内的应用对应，每个模块都有自己的template文件
>>common模块中的index.html是最基础的html文件，所有的html文件都是围绕着它进行的

>utils
>>封装的常用公共方法

>config
>>存放着数据库的配置文件，如果要连接mysql库
config.py: mysql_message = {'ENGINE': 'django.db.backends.mysql', 'NAME': '', 'USER': '', 'PASSWORD': '', 'HOST': '', 'PORT': '***'}

>logs
>>日志存放路径






