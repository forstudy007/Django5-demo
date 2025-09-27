#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/9/14 22:42
@Author  : 冲刺月入1万2
@Desc    : 自定义中间件：
"""
from django.utils.deprecation import MiddlewareMixin


class Md1(MiddlewareMixin):
    def process_request(self, request):
        print('request请求来了')

    def process_response(self, request, response):
        print('请求处理完毕，将返回到页面')
        return response
