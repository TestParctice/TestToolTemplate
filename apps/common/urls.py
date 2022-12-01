from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="common_index_page"),
    path('get_message', views.get_message_page, name="common_message_page"),
    path('get_all_message', views.get_all_message, name="common_get_all_message"),
    path('get_message_by_type', views.get_message_by_type, name="common_get_message_by_type"),
    path('monkey', views.get_monkey_page, name="common_get_monkey_page"),
    path('get_monkey', views.get_monkey, name="common_get_monkey_command"),
]
