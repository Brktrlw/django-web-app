from django.shortcuts import render
from .forms import BlogForm


def v_CreatePost(request):
    form = BlogForm(request.POST or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.postAuthor=request.user
        article.save()
        return render(request,"homePage.html")
    return render(request,"createPost.html")



