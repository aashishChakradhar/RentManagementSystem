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
from django.contrib import admin
from django.urls import path, include
from rent import views


urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('home/', views.Index.as_view(),name='home'),
    # path('admin/', admin.site.urls,name='admin'),
    path('login/', views.Login.as_view(),name='login'),
    path('logout/', views.Logout.as_view(),name='logout'),
    path('add-rent/', views.AddRent.as_view(),name='add-rent'),

    path('building/select/', views.SelectBuilding.as_view(),name='select-building'),
    path('building/add/', views.AddBuilding.as_view(),name='add-building'),
    path('building/update/<str:building_name>/', views.UpdateBuilding.as_view(), name='update-building'),
    path('building/delete/<str:building_name>/', views.DeleteBuilding.as_view(), name='delete-building'),

    path('view-rent/', views.ViewRentHistory.as_view(),name='view-rent'),
    path('backup-action/', views.BackupAction.as_view(),name='backup-action'),
]
