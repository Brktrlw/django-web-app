
from django.urls import path,include
from . import views
urlpatterns = [
    path("login",views.v_login,name='login'),
    path("logout",views.v_logout,name="logout"),

]
