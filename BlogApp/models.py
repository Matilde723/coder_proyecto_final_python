
from django.db import models
from django.template.defaultfilters import slugify

# Modelo base:
class Page(models.Model):
    title = models.CharField(max_length=200)
    subtilte = models.CharField(max_length=200)
    content = models.TextField()
  
    #def save(self, *args, **kwargs):
     #   if not self.slug:
      #      self.slug = slugify(self.title)
       # super().save(*args, **kwargs)

    class Meta:
        abstract = True #Clase base abstracta 

#Heredar Page, para una pag que contenga un artículo
class ArticlePage(Page):
    author = models.CharField(max_length=100)
    publish_date = models.DateField()

#Heredar Page, para una pag que contenga un blog
class BlogPage(Page):
    author = models.CharField(max_length=100)
    publish_date = models.DateTimeField(auto_now_add=True)
    