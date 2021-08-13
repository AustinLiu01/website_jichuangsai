from django.contrib import admin

# Register your models here.
#告诉后台需要导入一个数据表管理
from .models import DataPost
#在admin中注册此数据表
admin.site.register(DataPost)