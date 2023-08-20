from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=1000)
    content = FroalaField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    Blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="all_comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE )     
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add= True)
    like = models.ManyToManyField(User, related_name="liked_cmnts", blank=True)


class Like(models.Model):
    cmnt = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to="static/images")