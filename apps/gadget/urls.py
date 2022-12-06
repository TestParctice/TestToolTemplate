from django.urls import path

from . import views

urlpatterns = [
    path('urlchange', views.get_urlchange_page, name="gadget_get_urlchange_page"),
]
