
from django.urls import path,include
from . import views

urlpatterns = [
    path("create/",views.v_CreatePost,name="createPost")
]
