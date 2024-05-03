# urls

from django.contrib import admin
from django.urls import path
from .views import (article_create_view, 
                    blog_create_view,
                      article_list_view, 
                      article_update_view, 
                      article_delete_view,
                      blog_update_view, 
                      blog_delete_view,
                      pages_list_view, 
                      page_detail_view,
                      blog_list_view, 
                      home_view, 
                      acerca_de_mi,
                      signup_view) 
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', acerca_de_mi, name='about'),

    #Login/Logout/Signup:
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('accounts/signup/', signup_view, name='signup'),

    # Article CRUD
    path('articles/', article_list_view, name='articles-list'),
    path('create-article/', article_create_view, name='create-article'),
    path('update-article/<int:id>/', article_update_view, name='update-article'),
    path('delete-article/<int:id>/', article_delete_view, name='delete-article'),

    # Blog CRUD
    path('blogs/', blog_list_view, name='blogs-list'),
    path('create-blog/', blog_create_view, name='create-blog'),
    path('update-blog/<int:id>/', blog_update_view, name='update-blog'),
    path('delete-blog/<int:id>/', blog_delete_view, name='delete-blog'),

    # Pages list and detail views
    path('pages/', pages_list_view, name='pages-list'),
    path('pages/<int:page_id>/', page_detail_view, name='page-detail'),

]    