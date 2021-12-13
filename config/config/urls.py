
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.v_homePage ,name="homePage"),
    path("user/",include("USERS.urls")),
    path("contact/",views.v_homePage,name="contact")

]
