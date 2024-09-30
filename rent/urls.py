"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rent import views


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('home/', views.Index.as_view(),name='home'),
    path('logout/', views.Logout.as_view(),name='logout'),
    path('login/', views.Login.as_view(),name='login'),
    path('add-rent/', views.AddRent.as_view(),name='add-rent'),
  
]
