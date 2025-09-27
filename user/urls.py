#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/9/15 23:35
@Author  : 冲刺月入1万2
@Desc    : 
"""
from django.contrib import admin
from django.urls import path

from user import views

app_name = 'user'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
]
