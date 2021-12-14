from django.shortcuts import render,redirect
from .forms import BlogForm


def v_CreatePost(request):
    form=BlogForm()
    return render(request,"createPost.html",{"form":form})




