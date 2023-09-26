# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def blog(request):
    print('blog')
    context = {
        'text' : 'Olá blog'
    }
    return render(
        request,
        'blog/index.html',
        context,
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