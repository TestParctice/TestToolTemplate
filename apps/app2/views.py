from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest


def get_invalidpurchasecontract_page(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'invalidpurchasecontract.html')


def get_stauts_by_invalidpurchasecontractid(request):
    if request.method == 'POST':
        purchasecontract = request.POST.get("purchasecontract")
    res = {}
    if res["purchasestatus"] == '采购合同id错误，未查询到数据':
        return JsonResponse({"res": res})
    else:
        if res["purchasestatus"] == 1:
            res["purchasestatus"] = "采购合同状态为有效状态"
        elif res["purchasestatus"] == 2:
            res["purchasestatus"] = "采购合同状态为无效状态"
        else:
            temp = res["purchasestatus"]
            res["purchasestatus"] = "数据库中状态为：%s,找开发检查数据" % temp
    if res["goodstocksStatus"] == 1:
        res["goodstocksStatus"] = "货品状态为有效状态"
    elif res["goodstocksStatus"] == 2:
        res["goodstocksStatus"] = "货品状态为无效状态"
    else:
        temp = res["goodstocksStatus"]
        res["goodstocksStatus"] = "数据库中状态为：%s,找开发检查数据" % temp
    if res["commoditiesStatus"] is None:
        res["commoditiesStatus"] = "没有包装过商品"
    else:
        res["commoditiesStatus"] = list(set(res["commoditiesStatus"]))
    if res["commodityPagesMsg"] is None:
        res["commodityPagesMsg"] = "没有商品摆放在页面上"
    else:
        res["commodityPagesMsg"] = "存在商品摆放在页面上"
    return JsonResponse({"res": res})
