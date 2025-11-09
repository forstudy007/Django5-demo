#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2025/9/27 15:24
@Author  : 冲刺月入1万2
@Desc    : 表单视图
"""
from django import forms
from django.forms import ModelForm, Form

from helloWorld.models import StudentInfo, BookTypeInfo, BookInfo


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


# 图书表单
class BookInfoForm(Form):
    bookName = forms.CharField(max_length=20, label="图书名称")
    price = forms.FloatField(label="图书价格")
    publishDate = forms.DateField(label="出版日期")
    # 获取图书类别列表
    bookTypeList = BookTypeInfo.objects.values()
    # 图书类别以下拉框形式显示，下拉框选项id是图书类别id，下拉框选项文本是图书类别名称
    choices = [(v['id'], v['bookTypeName']) for v, v in enumerate(bookTypeList)]
    bookType_id = forms.ChoiceField(required=False, choices=choices, label="图书类别")


# 配置中心
class BookInfoModelForm(ModelForm):
    class Meta:
        model = BookInfo
        fields = '__all__'
        widgets = {
            'bookName': forms.TextInput(attrs={'placeholder': '请输入用户名', 'id': 'bookName', 'class': 'inputClass'}),
        }
        labels = {
            'bookName': '图书名称',
            'price': '图书价格',
            'publishDate': '出版日期',
            'bookType': '图书类别'
        }
        help_texts = {
            'bookName': '请输入图书名称'
        }
