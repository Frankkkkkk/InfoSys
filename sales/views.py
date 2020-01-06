from django.http import HttpResponse
from django.shortcuts import render

def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")