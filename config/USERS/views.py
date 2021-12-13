from django.shortcuts import render
from django.contrib.auth import logout


def v_login(request):
    return render(request,"login.html")

def v_logout(request):
    logout(request)
    return render(request,"homePage.html")

def v_register(request):
    return render(request,"register.html")
