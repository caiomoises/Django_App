from django.http import HttpResponse

# from django.shortcuts import render
# Create your views here.

def blog(request):
    print('blog')
    return HttpResponse('Blog do App 1')

def exemplo(request):
    print('Exemplo')
    return HttpResponse('Exemplo do blog 1')