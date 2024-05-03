#views

from django.shortcuts import render, redirect
from .forms import ArticlePageForm, BlogPageForm
from .models import ArticlePage, BlogPage
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, user_passes_test

#Decorator para que solo el administrador tenga funcioanlidad CRUD:
def admin_required(login_url=None):
    return user_passes_test(lambda u: u.is_superuser, login_url=login_url)

#Acerca de Mi:
def acerca_de_mi(request):
    content = '<p>Acerca de mí: Me llamo Matilde Ocampo, soy originaria de la ciudad de México, y trabajo como Data Analist para Att Internacional, mi interés en aprender Python ha sido para poder automatizar procesos y reportes en mi trabajo.</p>'
    return HttpResponse(content)

#View para la home page:

def home_view(request):
    return render(request, 'home.html')

#-------------------------------------------------------------------------------
#CRUD:
# Views para crear articulos y blogs:

@login_required(login_url='/accounts/login/')
@admin_required(login_url='/accounts/login/')
def article_create_view(request):
    if request.method == 'POST':
        form = ArticlePageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles-list')  # Redireciona a la lsita de articulos depués de salvar
    else:
        form = ArticlePageForm()
    return render(request, 'article_create.html', {'form': form})


@login_required(login_url='/accounts/login/')
@admin_required(login_url='/accounts/login/')
def blog_create_view(request):
    if request.method == 'POST':
        form = BlogPageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs-list')  # Redireciona a la lista de blogs después de salvar
    else:
        form = BlogPageForm()
    return render(request, 'blog_create.html', {'form': form})

#--------------------------------------------------------------------
#Views para busqueda en la base de datos 

@login_required(login_url='/accounts/login/')
@admin_required(login_url='/accounts/login/')
def article_list_view(request):
    search_query = request.GET.get('search', '')
    if search_query:
        articles = ArticlePage.objects.filter(title__icontains=search_query)
    else:
        articles = ArticlePage.objects.all()
    return render(request, 'article_list.html', {'articles': articles})

@login_required(login_url='/accounts/login/')
@admin_required(login_url='/accounts/login/')
def blog_list_view(request):
    search_query = request.GET.get('search', '')
    if search_query:
        blogs = BlogPage.objects.filter(title__icontains=search_query)
    else:
        blogs = BlogPage.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})

#------------------------------------------------------------------------
#Update View
@login_required(login_url='/accounts/login/')
@admin_required(login_url='/accounts/login/')
def article_update_view(request, id):
    article = ArticlePage.objects.get(id=id)
    if request.method == 'POST':
        form = ArticlePageForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles-list')
    else:
        form = ArticlePageForm(instance=article)
    return render(request, 'article_update.html', {'form': form})

@login_required(login_url='/accounts/login/')
@admin_required(login_url='/accounts/login/')
def blog_update_view(request, id):
    blog = BlogPage.objects.get(id=id)
    if request.method == 'POST':
        form = BlogPageForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blogs-list')
    else:
        form = BlogPageForm(instance=blog)
    return render(request, 'blog_update.html', {'form': form})

#-------------------------------------------------------------------------
#Delete View
@login_required(login_url='/accounts/login/')
@admin_required(login_url='/accounts/login/')
def article_delete_view(request, id):
    article = ArticlePage.objects.get(id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('articles-list')
    return render(request, 'article_delete_confirm.html', {'article': article})

@login_required(login_url='/accounts/login/')
@admin_required(login_url='/accounts/login/')
def blog_delete_view(request, id):
    blog = BlogPage.objects.get(id=id)
    if request.method == 'POST':
        blog.delete()
        return redirect('blogs-list')
    return render(request, 'blog_delete_confirm.html', {'blog': blog})

#-----------------------------------------------------------------------
#View para el user registration
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Optionally, add user to group or handle additional logic
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

#-----------------------------------------------------------------------
#View para la lista de Articulos y Blogs
@login_required(login_url='/accounts/login/')
def pages_list_view(request):
    articles = ArticlePage.objects.all()
    blogs = BlogPage.objects.all()
    return render(request, 'pages_list.html', {'articles': articles, 'blogs': blogs})
#-----------------------------------------------------------------------
#View para la lista de detalles por Articulos y Blogs
@login_required(login_url='/accounts/login/')
def page_detail_view(request, page_id):
    try:
        article = ArticlePage.objects.get(id=page_id)
        return render(request, 'article_detail.html', {'article': article})
    except ArticlePage.DoesNotExist:
        try:
            blog = BlogPage.objects.get(id=page_id)
            return render(request, 'blog_detail.html', {'blog': blog})
        except BlogPage.DoesNotExist:
            return HttpResponse('There are no available pages yet', status=404)
        



