#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/9/15 23:37
@Author  : 冲刺月入1万2
@Desc    : 
"""
from django.contrib import admin
from django.urls import path

from order import views

app_name = 'order'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('list/<int:year>/<int:month>/<int:day>/', views.list, name='list'),
]
