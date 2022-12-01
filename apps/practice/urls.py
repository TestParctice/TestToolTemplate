from django.urls import path

from . import views

urlpatterns = [
    path('get_webelements', views.get_webelements_page, name="practice_get_webelements_page"),
    path('get_loation', views.get_loation_page, name="practice_get_loation_page"),
]
