from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.CharField(max_length=12)
    slug = models.SlugField(max_length=78)
    timestamp = models.DateTimeField(blank=True)

