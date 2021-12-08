from django.urls import path

from .views import vPosts,vPostCreate,vPostDetail

urlpatterns = [
    path('',vPosts,name="posts"),
    path('create/',vPostCreate),
    path('<str:PostName>/',vPostDetail)
]