from django.shortcuts import render
from django.shortcuts import HttpResponse  # 导入HttpResponse模块
# Create your views here.

def index(request):
    # request 参数必须存在，类似self的规则。可以改，用于封装用户请求。
    # request.POSt
    # request.GET
    return HttpResponse("Hello Yuan Xin ! ")
    # 不能直接返回字符串，必须是由这个类封装。这是django的规则，不是python的规则。