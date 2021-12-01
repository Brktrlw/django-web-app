
from django.contrib import admin
from django.urls import include
from django.urls import path
from .views import mainIndex,about
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/',include("blog.urls")),
    path("",mainIndex,name="mainIndex"),
    path("about/",about,name="about"),
    path("user/",include("UserApp.urls"))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
