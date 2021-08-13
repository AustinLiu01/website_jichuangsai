from django.urls import path
from . import views
# 正在部署的应用名称
app_name = 'data2display'

urlpatterns = [
    path('data_list/', views.data_list, name='data_list'),
]
