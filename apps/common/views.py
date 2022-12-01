from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from apps.common.services import messageService


def index(request: HttpRequest):
    return render(request, "common/index.html")


def get_message_page(request: HttpRequest):
    res = messageService.get_all_message()
    return render(request, "common/message.html", context=res)


def get_all_message(request):
    if request.method == 'GET':
        res = messageService.get_all_message()
        return JsonResponse(res)


def get_message_by_type(request):
    if request.method == 'POST':
        message_type = request.POST.get("type")
        if type is not None:
            res = messageService.get_message_by_type(type=message_type)
        else:
            res = messageService.get_all_message()
            if res is None:
                res = {"type": "检查type类型"}
    return JsonResponse(res)


def get_monkey_page(request: HttpRequest):
    return render(request, template_name="common/monkey.html")


def get_monkey(request):
    if request.method == 'GET':
        packageName = request.GET['packageName']
        ytime = request.GET['ytime']
        acount = request.GET['acount']
        seed = request.GET['seed']
        touch = request.GET['touch']
        motion = request.GET['motion']
        trackball = request.GET['trackball']
        nav = request.GET['nav']
        najornav = request.GET['najornav']
        syskeys = request.GET['syskeys']
        appswitch = request.GET['appswitch']
        anyevent = request.GET['anyevent']
        bk = request.GET['bk']
        cs = request.GET['cs']
        suc = request.GET['suc']
        err = request.GET['err']
        if packageName == "":
            text_monkey = "包名为空,请输入包名，否则生成的monkey命令没有任何意义"
            return JsonResponse({"text_monkey": text_monkey})
        elif int(acount) <= 0:
            text_monkey = "执行次数必须为正整数，请输入执行次数（正整数），否则生成的monkey命令没有任何意义"
            return JsonResponse({"monkey": text_monkey})
        else:
            text_monkey = "adb shell monkey  --ignore-crashes  --ignore-timeouts " + packageName + " " + acount
            if ytime != " ":
                text_monkey = text_monkey + " --throttle" + ytime
            if seed != " ":
                text_monkey = text_monkey + " -s " + seed
            if touch != " ":
                text_monkey = text_monkey + " --pct-touch " + touch
            if motion != "":
                text_monkey = text_monkey + " --pct-motion " + motion
            if trackball != "":
                text_monkey = text_monkey + " --pct-trackball " + trackball
            if nav != "":
                text_monkey = text_monkey + " --pct-nav " + nav
            if najornav != "":
                text_monkey = text_monkey + " --pct-majornav " + najornav
            if syskeys != "":
                text_monkey = text_monkey + " --pct-syskeys " + syskeys
            if appswitch != "":
                text_monkey = text_monkey + " --pct-appswitch " + appswitch
            if anyevent != "":
                text_monkey = text_monkey + " --pct-anyevent " + anyevent
            if suc != "":
                text_monkey = text_monkey + " 1> " + suc
            if err != "":
                text_monkey = text_monkey + " 2> " + err
        return JsonResponse({"text_monkey": text_monkey})
