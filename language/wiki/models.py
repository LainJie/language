from django.db import models
from django.template.defaultfilters import slugify
import random
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField()
    likes = models.IntegerField()
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if not self.slug:
            self.slug = self.name.replace(' ', '-')
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
       return self.name
   
class Page(models.Model):
       category = models.ForeignKey(Category)
       title = models.CharField(max_length=128,unique=True)
       url = models.URLField()
       views = models.IntegerField(default=0)
       
       def __str__(self):
           return self.title