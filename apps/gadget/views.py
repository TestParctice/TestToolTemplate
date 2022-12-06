from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest


def get_urlchange_page(request: HttpRequest):
    return render(request, "gadget/urlchange.html")
