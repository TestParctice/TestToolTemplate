from django.urls import path

from . import views

urlpatterns = [
    # path('queryzones', views.get_queryzones_page),
    path('', views.get_invalidpurchasecontract_page),
]
