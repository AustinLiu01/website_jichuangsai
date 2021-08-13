from django.shortcuts import render
from django.http import HttpResponse
from .models import DataPost
from django.core.paginator import Paginator

def data_list(request):
    # 取出所有数据
    data_lst = DataPost.objects.all()
    # 分页,每页显示10条记录
    paginator = Paginator(data_lst, 10)
    # 获取url中的页码
    page = request.GET.get('page')
    # 将导航对象相应的页码内容返回给 data
    data = paginator.get_page(page)
    # 需要传递给模版的对象
    context = {'data': data}
    # render函数：载入模版，并返回context对象
    '''
    request是固定的request对象，照着写就可以
    data2display/list.html定义了模板文件的位置、名称
    context定义了需要传入模板文件的上下文
    '''
    return render(request, 'data2display/list.html', context)
