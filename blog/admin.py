from django.contrib import admin
from .models import BlogModel,KategoriModel,CommentModel,ContactModel

admin.site.register(KategoriModel)
admin.site.register(BlogModel)


class YorumAdmin(admin.ModelAdmin):
    list_display = ('commentAuthor','blogId','createdTime')
    search_fields = ('commentAuthor__username',)

class IletisimAdmin(admin.ModelAdmin):
    list_display = ('title','email','sendTime')
    search_fields = ('email',)

admin.site.register(CommentModel,YorumAdmin)
admin.site.register(ContactModel,IletisimAdmin)