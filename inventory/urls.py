from django.contrib import admin
from django.urls import path
from inventory import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('login', views.loginUser, name='login'),
    path('signup', views.register, name='signup'),
]