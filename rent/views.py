from django.shortcuts import render, redirect,HttpResponse
from django.views import View

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

from rent.models import *

# Create your views here.



class Index(View):
    def get(self, request):
        context = {
            "page_name":"home",
            "app_name":"myRent",
        }
        return render(request,'index.html',context)