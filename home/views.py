# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    print('HOME')
    context = {
            'text': 'GABAS DEV'
        }
    return render(
        request,
        'home/index.html',
        context,
    )
