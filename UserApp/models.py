from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUserModel(AbstractUser):
    avatar= models.ImageField(upload_to="Users_Image",blank=True,null=True,default="default.jpg")

    class Meta:
        db_table="User"
        verbose_name="Kullanıcı"
        verbose_name_plural="Kullanıcılar"

    def __str__(self):
        return self.username