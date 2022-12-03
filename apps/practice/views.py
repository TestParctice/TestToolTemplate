from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from utils.ip import get_ip
from apps.practice.services.APIService import APIService


def get_webelements_page(request: HttpRequest):
    return render(request, "practice/webelements.html")


def get_loation_page(request: HttpRequest):
    return render(request, "practice/location.html")


def get_api_request(request: HttpRequest):
    ip = get_ip()

    return render(request, template_name="practice/API.html",
                  context={'ip': "ip", "params_typelist": ['json', 'text', 'jsonp'], "typelist": ["get", "post"]})


def preservation_api_msg(request):
    print("开始执行")
    res_data = request.POST.get("res_data")
    print(res_data)
    url = request.POST.get("url")
    params = request.POST.get("params")
    api_type = request.POST.get("api_type")
    dataType = request.POST.get("dataType")
    header = request.POST.get("header")
    res = APIService().save_api_info(url=url, params=params, responseDaa=res_data, apiType=api_type, header=header,
                                     apiParamsType=dataType)
    print(res)
    if res is True:
        return JsonResponse({"res_data": res_data})
    else:
        print(res)
        return JsonResponse({"res_data": res_data})
