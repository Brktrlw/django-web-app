from django.urls import path
from .views import registerPage,loginPage,userProfilePage,userLogout
app_name="UserApp"

urlpatterns=[
    path("register/",registerPage,name="registerPage"),
    path("login/",loginPage,name="loginPage"),
    path("",userProfilePage,name="userProfilePage"),
    path("logout/",userLogout,name="userLogout")
]

