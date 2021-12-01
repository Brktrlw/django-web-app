
from django.contrib import admin
from django.urls import include
from django.urls import path
from .views import mainIndex,about
urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',include("blog.urls")),
    path("",mainIndex,name="mainIndex"),
    path("about/",about,name="about"),
    path("user/",include("UserApp.urls"))
]
