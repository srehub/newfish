from django.shortcuts import render
from django.shortcuts import HttpResponse
# 导入HttpResponse模块,作用是显示内容到网页上，如 print
# Create your views here.

user_list = [
    {"user":"kitty","pwd":"hello"},
]

def index(request):
    # request 参数必须存在，类似self的规则。可以改，用于封装用户请求。
    # request.POSt
    # request.GET
    # return HttpResponse("Hello Yuan Xin ! ")
    # 不能直接返回字符串，必须是由这个类封装。这是django的规则，不是python的规则。
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        temp = {"user":username,"pwd":password}
        user_list.append(temp)
    return render(request, "index.html", {"data":user_list})