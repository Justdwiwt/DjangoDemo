from django.db import models


# Create your models here.

# 定义信息发布表
# content   保存消息的内容
# user_name 保存发布人的名字
# kind      保存消息的类型
class Moment(models.Model):
    content = models.CharField(max_length=200)
    user_name = models.CharField(max_length=20)
    kind = models.CharField(max_length=20)
