from django.urls import path

from . import views

urlpatterns = [
    path('/index', views.index, name="app1_index_page"),
]
