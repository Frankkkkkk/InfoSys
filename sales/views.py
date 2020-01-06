from django.http import HttpResponse


def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。")

def listorders1(request):
    return HttpResponse("下面是系统中所有的订单信息。。。1")

def listorders2(request):
    return HttpResponse("下面是系统中所有的订单信息。。。2")

def listorders3(request):
    return HttpResponse("下面是系统中所有的订单信息。。。3")

