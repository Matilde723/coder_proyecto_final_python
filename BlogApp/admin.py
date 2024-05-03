from django.contrib import admin

# Register your models here.
from .models import ArticlePage, BlogPage

admin.site.register(ArticlePage)
admin.site.register(BlogPage)




