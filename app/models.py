# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

# Create your models here.

# 新增元组用于设置消息类型枚举项

KIND_CHOICES = (
    ('python技术', 'python技术'),
    ('数据库技术', '数据库技术'),
    ('经济学', '经济学'),
    ('文体资讯', '文体资讯'),
    ('个人心情', '个人心情'),
    ('其他', '其他'),
)


# 定义信息发布表
# content   保存消息的内容
# user_name 保存发布人的名字
# kind      保存消息的类型
class Moment(models.Model):
    content = models.CharField(max_length=300)
    user_name = models.CharField(max_length=20, default='匿名')
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])
