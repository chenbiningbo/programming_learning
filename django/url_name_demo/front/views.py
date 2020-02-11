from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, reverse

# Create your views here.

def index(request):
    # ?username=XXX
    username = request.GET.get('username')
    if username:
        return HttpResponse('前台首页')
    else:
        return redirect(reverse('front:login'))

def login(request):
    return HttpResponse('前台登录页面')