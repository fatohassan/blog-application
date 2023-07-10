from django.db import models
from django.utils.text import slugify

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    company = models.CharField(max_length=200)



class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    slug = models.SlugField(null=True, max_length=40, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug= slugify(self.title)
        return super(BlogPost, self).save(*args, **kwargs)
    def __str__(self):
        return self.title

 