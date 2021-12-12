from django.db import models

class PostModel(models.Model):
    postAuthor      = models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    postTitle       = models.CharField(max_length=100,verbose_name="Post Başlığı")
    postDescription = models.TextField(max_length=500,)
    postCreatedDate = models.DateTimeField(auto_now_add=True)
    postEditedDate  = models.DateTimeField(auto_now=True)


