# -*- encoding: utf-8 -*-
from django.urls import path

from . import models

from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('hello_tpl', views.hello_tpl),
]