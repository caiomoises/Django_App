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

def post(request, post_id):
    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break
    

    context = {
        # 'text': 'Blog de notícias',
        'post': found_post,
        'title': found_post['title'] + ' - '
    }

    return render(
        request,
        'blog/post.html',
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