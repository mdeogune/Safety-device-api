from django.conf.urls import url, include
from django.contrib import admin

from .views import *
from . import views

urlpatterns = [
      url(r'^', IndexView),
    ]

   