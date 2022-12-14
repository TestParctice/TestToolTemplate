from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("common.urls")),
    path('common/', include("common.urls")),
    path('practice/', include("practice.urls")),
    path('gadget/', include("gadget.urls")),
]
