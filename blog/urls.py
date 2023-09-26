from django.urls import path
from blog import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='home'),
    path('post/<int:id>', views.post, name='post'),
    path('exemplo/', views.exemplo, name='exemplo')
]