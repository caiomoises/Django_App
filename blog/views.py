# from django.http import HttpResponse
from blog.data import posts
from django.shortcuts import render


def blog(request):
    print('blog')

    context = {
        # 'text': 'Blog de notícias',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )

def post(request, id):
    print('post', id)

    context = {
        # 'text': 'Blog de notícias',
        'posts': posts
    }

    return render(
        request,
        'blog/index.html',
        context
    )

def exemplo(request):
    print('exemplo')

    context = {
        'text': 'Olá exemplo',
        'title': 'Essa é uma página de exemplo - ',
    }

    return render(
        request,
        'blog/exemplo.html',
        context
    )