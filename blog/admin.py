from django.contrib import admin
from .models import BlogModel,KategoriModel,CommentModel

admin.site.register(KategoriModel)
admin.site.register(BlogModel)


class YorumAdmin(admin.ModelAdmin):
    list_display = ('commentAuthor','blogId','createdTime')
    search_fields = ('commentAuthor__username',)

admin.site.register(CommentModel,YorumAdmin)