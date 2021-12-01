from django.urls import path

from .views import vPosts,vPostCreate,vPostDetail

urlpatterns = [
    path('',vPosts),
    path('create/',vPostCreate),
    path('<str:PostName>/',vPostDetail)
]