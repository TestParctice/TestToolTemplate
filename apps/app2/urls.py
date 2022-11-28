from django.urls import path

from . import views

urlpatterns = [
    path('/index', views.index, name="app2_index_page"),
]
