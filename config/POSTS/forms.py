

from django import forms
from .models import PostModel

class BlogForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields=["postTitle","postDescription","postAuthor"]




