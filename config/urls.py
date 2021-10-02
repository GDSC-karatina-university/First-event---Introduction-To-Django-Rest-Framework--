
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    url('api/(?P<version>(v1|v2))/',include("api.routes.urls"))
]
