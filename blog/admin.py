from django.contrib import admin
from .models import BlogModel,KategoriModel

admin.site.register(KategoriModel)
admin.site.register(BlogModel)
