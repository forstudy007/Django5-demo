#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/9/27 15:24
@Author  : 冲刺月入1万2
@Desc    : 表单视图
"""
from django import forms
from django.forms import ModelForm

from helloWorld.models import StudentInfo


# 定义学生form表单
class StudentForm(ModelForm):
    # 配置中心
    class Meta:
        # 关联模型
        model = StudentInfo
        # 指定字段（或用 '__all__' 表示所有字段）
        fields = '__all__'
        # fields = ['name', 'age']
        # 自定义表单控件样式
        widgets = {
            'name': forms.TextInput(attrs={'id': 'name', 'class': 'inputClass'}),
            'age': forms.NumberInput(attrs={'id': 'age'})
        }
        # 字段标签
        labels = {
            'name': '姓名',
            'age': '年龄'
        }
