from django.http import HttpResponse
from django.shortcuts import redirect, reverse

# Create your views here.

def index(request):
    username = request.GET.get('username')
    if username:
        return HttpResponse('CMS首页')
    else:
        return redirect(reverse('cms:login'))

def login(request):
    return HttpResponse('CMS登录页面')