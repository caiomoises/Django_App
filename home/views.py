from django.http import HttpResponse

# from django.shortcuts import render
# Create your views here.

def home(request):
    print('HOME')
    return HttpResponse('HOME do App 1')
