from django.shortcuts import render,HttpResponse
from .models import BlogModel


def vPosts(request):
    blogs=BlogModel.objects.all()
    return render(request,"Posts.html",{"blogs":blogs})

def vPostCreate(request):
    return HttpResponse("/Posts/Create/")

def vPostDetail(request,PostName):
    return HttpResponse(str(PostName)+str(" naber"))