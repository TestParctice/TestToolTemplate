from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest


def get_webelements_page(request: HttpRequest):
    return render(request, "practice/webelements.html")


def get_loation_page(request: HttpRequest):
    return render(request, "practice/location.html")
