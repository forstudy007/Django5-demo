from django.http import HttpResponse
from django.urls import reverse, resolve


# Create your views here.
def index(request):
    route_url = reverse('order:index')
    print("reverse反向解析得到路由地址：" + route_url)
    result = resolve(route_url)
    print("resolve通过路由地址得到路由信息：" + str(result))
    return HttpResponse("订单信息")


def list(request, year, month, day):
    kwargs = {'year': year - 1, 'month': month + 1, 'day': day}
    args = [year, month, day]
    # route_url = reverse('order:list', args=args)
    route_url = reverse('order:list', kwargs=kwargs)
    print("reverse反向解析得到路由地址；" + route_url)
    result = resolve(route_url)
    print("resolve通过路由地址得到路由信息" + str(result))
    return HttpResponse("订单列表")
