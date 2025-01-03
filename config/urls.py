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
# from rent.views import AdminView

admin.site.site_header = "My Rent Admin"
admin.site.site_title = "Admin Portal"
admin.site.index_title = "My Club"

urlpatterns = [
    path('admin/', admin.site.urls, name = 'admin'),
    # path('', include(('club.urls', 'club'), namespace='club')),
    # path('admin-redirect/', AdminView.as_view(), name='admin-redirect'),  # Custom redirect view
    path('', include(('rent.urls', 'rent'), namespace='rent')), 
]
