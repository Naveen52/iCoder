from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.CharField(max_length=12)
    slug = models.SlugField(max_length=78)
    timestamp = models.DateTimeField(blank=True)
    def __str__(self):
        return self.title
    

class blogComments(models.Model):
    sno = models.AutoField(primary_key=True)
    comment= models.TextField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp= models.DateTimeField(default=now)
