from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest


def index(request: HttpRequest):
    return render(request, "common/index.html")
