from django.shortcuts import render,HttpResponse



def vPosts(request):
    return HttpResponse("/Posts")

def vPostCreate(request):
    return HttpResponse("/Posts/Create/")

def vPostDetail(request,PostName):
    return HttpResponse(str(PostName)+str(" naber"))