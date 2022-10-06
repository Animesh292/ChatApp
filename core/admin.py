from django.contrib import admin

# Register your models here.
from django import VERSION
from django.urls import include, path
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
]
