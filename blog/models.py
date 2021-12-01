from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

class KategoriModel(models.Model):
    title      =models.CharField(max_length=50,verbose_name="Kategori",blank=False,null=False,unique=True)
    class Meta:
        verbose_name_plural="Kategoriler"
        db_table="Kategoriler"
    def __str__(self):
        return self.title


class BlogModel(models.Model):
    author     =models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar",blank=False,null=False)
    title      =models.CharField(max_length=100,verbose_name="Başlık",blank=False,help_text="Başlık Bilgisi")
    description=RichTextField()
    createdDate=models.DateTimeField(auto_now_add=True,auto_now=False)
    editedDate =models.DateTimeField(auto_now=True)
    slug       =AutoSlugField(unique=True,populate_from="title")
    categories =models.ManyToManyField(KategoriModel,related_name="Blog",null=False,blank=False)
    images     =models.ImageField(upload_to="BlogResimleri",null=True,blank=True)

    class Meta:
        verbose_name_plural="Bloglar"
        ordering=["id"]
        db_table = "Blog"

    def __str__(self):
        return self.title

class CommentModel(models.Model):
    commentAuthor = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yorum Sahibi",blank=True,null=True)
    commentText   = models.TextField(max_length=150,verbose_name="Yorum İçeriği",blank=True,null=True)
    blogId        = models.ForeignKey(BlogModel,on_delete=models.CASCADE,blank=False,null=False)
    createdTime   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="Comments"
        verbose_name="Yorum"
        verbose_name_plural="Yorumlar"

    def __str__(self):
        return self.commentText
















