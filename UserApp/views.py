from django.shortcuts import render,HttpResponse

def registerPage(request):
    return HttpResponse("Register page")


def loginPage(request):
    return HttpResponse("login page")


def userProfilePage(request):
    return HttpResponse("home page")

def userLogout(request):
    pass