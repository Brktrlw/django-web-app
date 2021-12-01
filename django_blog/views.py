from django.shortcuts import render


def about(request):
    return render(request,"about.html")
def mainIndex(request):
    return render(request,"mainIndex.html")