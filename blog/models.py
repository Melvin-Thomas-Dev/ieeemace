from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class BlogPost(models.Model):
    title=models.CharField(max_length=150,blank=False)
    topic=models.CharField(max_length=150)
    author=models.ForeignKey(User, related_name='user',on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)
    content=models.TextField(blank=False)
    slug=models.SlugField()

    def __str__(self):
        return self.title