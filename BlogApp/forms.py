from django import forms
from .models import ArticlePage, BlogPage

class ArticlePageForm(forms.ModelForm):
    class Meta:
        model = ArticlePage
        fields = ['title', 'subtitle', 'content', 'author', 'publish_date']

class BlogPageForm(forms.ModelForm):
    class Meta:
        model = BlogPage
        fields = ['title', 'subtitle', 'content', 'author', 'publish_date']