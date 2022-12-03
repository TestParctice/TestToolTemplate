from django.urls import path

from apps.practice import views

urlpatterns = [
    path('get_webelements', views.get_webelements_page, name="practice_get_webelements_page"),
    path('get_loation', views.get_loation_page, name="practice_get_loation_page"),
    path('get_api_request', views.get_api_request, name="practice_get_api_request_page"),
    path('preservation', views.preservation_api_msg, name="practice_preservation_api_msg"),

]
