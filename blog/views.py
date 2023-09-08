# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def blog(request):
    print('blog')
    return render(
        request,
        'blog.html',
                  )

def exemplo(request):
    print('Exemplo')
    return render(
        request,
        'exemplo.html',
    )