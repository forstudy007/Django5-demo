#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/10/18 22:25
@Author  : 冲刺月入1万2
@Desc    : 一定能行的
"""

from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import reverse
from jinja2 import Environment


def environment(**options):
    env = Environment(**options)
    # 注册全局函数（如 static、url）
    env.globals.update({
        'static': staticfiles_storage.url,  # 静态资源函数
        'url': reverse  # 路由反向解析函数
    })
    return env
