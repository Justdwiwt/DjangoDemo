from django.contrib import admin
from .models import Moment

# Register your models here.

# 逐个声明要管理的模型类
admin.site.register(Moment)
