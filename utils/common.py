import urllib.parse


def params_convert_to_dict(params: str):
    """将一长串的参数转化成字典"""
    # params = "app=p&sv=9&os=android"
    # 当参数里有转义字符时，要转义成[]类似的格式
    if "%" in params:
        params = urllib.parse.unquote(params)
    params = params.strip("&")
    try:
        results = {i.split("=")[0]: i.split("=")[1] for i in params.split("&")}
        return results
    except Exception as e:
        return str(type(e)) + ":" + str(e)


if __name__ == '__main__':
    print(params_convert_to_dict("app=p&sv=9&os=android"))
    print(params_convert_to_dict("app=p&sv=9&os=an&droid"))
