from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'clubname' : "collabyte"
        }
    return render(request,"index.html",context)