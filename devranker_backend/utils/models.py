# -*- encoding: utf-8 -*-
"""
--------------------------------------------------------
@File: models.py
@Project: dev-talent-ranker 
@Time: 2024/10/28   21:03
@Author: shelhen
@Email: shelhen@163.com
@Software: PyCharm 
--------------------------------------------------------
# @Brief:
"""
from django.db import models


class BaseModel(models.Model):
    """所有模型类的父类"""
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        # 说明该类是 抽象类，用于继承使用，不会在迁移时创建该类的表
        abstract = True