from django.urls import path, include
from club import views


urlpatterns = [
    path('', views.index,name='index'),
    path('index', views.index,name='index'),
    
]