# python
# -*- coding: UTF-8 -*-
"""
=================================================
@Project -> File   ：epidemic_analysis -> urls.py
@IDE    ：PyCharm
@Author ：Zhou DingJv
@Date   ：2021/6/23 16:37
@Desc   ：
==================================================
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page/index.html/id=<int:id>', views.detail, name='detail'),
    path('wordcloud',views.wordcloud, name='wordcloud'),
]
