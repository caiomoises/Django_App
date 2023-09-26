# from django.http import HttpResponse
from blog.data import posts
from django.shortcuts import render

# Create your views here.

def blog(request):
    print('blog')

    context = {
        'text' : 'Blog notícias', 
        'posts' : posts 
    }

    return render(
        request,
        'blog/index.html',
        context       
    )

def exemplo(request):
    print('Exemplo')
    context = {
        'text' : 'Olá exemplo',
        'title': 'Pagina de exemplo - '
    }
    return render(
        request,
        'blog/exemplo.html',
        context,
    )