from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', admin.site.urls),
    path('app1/', include("apps.app1.urls")),
    path('app2/', include("apps.app2.urls")),
]
