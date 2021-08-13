from django.db import models
# 导入内建的user模型
from django.contrib.auth.models import User
# timezone用于处理时间相关事务
from django.utils import timezone
# Create your models here.
# 统计数据模型


class DataPost(models.Model):
    # 药材名称。
    name = models.CharField(max_length=10, default="")
    # 药材重量。models.CharField 为字符串字段，用于保存较短的字符串，比如标题
    weight = models.FloatField()
    # 药材价格
    price = models.FloatField()
    # 数据上传时间。参数 default=timezone.now 指定其在创建数据时将默认写入当前的时间
    updated = models.DateTimeField(default=timezone.now)
    # 提供模型的元数据，即表的共同行为

    class Meta:
        ordering = ('-updated',)   # 时间倒序排列数据
    # 函数 __str__ 定义当调用对象的 str() 方法时的返回值内容

    def __str__(self):
        return self.name  # 返回上传的数据的标题
