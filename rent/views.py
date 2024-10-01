from django.shortcuts import render, redirect,HttpResponse
from django.views import View

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

from rent.models import *
from static.pythonfiles.calender import *
# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
class BaseView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = ''
    # redirect_field_name = 'redirect_to'

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect ('/')

class Login(View):
    def get(self,request):
        context = {
            "app_name":"myRent",
            "page_name":"login",
        }
        return render(request,'login.html',context)
    
    def post (self,request):
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username = username, password = password)
        if user is not None:# checks if the user is logged in or not?
            login(request,user) #logins the user
            return redirect ('/')
        else:
            return redirect(request.path)






class Index(BaseView):
    def get(self, request):
        if not request.user.is_authenticated:
            return render(request,'login.html')
        context = {
            "app_name":"myRent",
            "page_name":"home",
        }
        return render(request,'index.html',context)
    
class AddRent(BaseView):
    def get(self,request):
        context = {
            "page_name":"add-rent",
            "app_name":"myRent",
            "months" : Month(),
            "rooms": Room(),
        }
        
        return render(request,'rent.html',context)
    def post (self,request):
        try:
            submited_amount = request.POST.get('amount')
            submited_room = request.POST.get('room')
            submited_month = request.POST.get('month')
            submited_remarks = request.POST.get('remarks')
            print(submited_amount)
            print(submited_room)
            print(submited_month)
            print(submited_remarks)
            return redirect ('add-rent')
        except Exception as e:
            return redirect(request.path)
        
class ViewRent(BaseView):
    def get(self,request):
        context = {
            "page_name":"add-rent",
            "app_name":"myRent",
        }
        
        return render(request,'rent.html',context)
    def post (self,request):
        try:
            submited_amount = request.POST.get('amount')
            submited_room = request.POST.get('room')
            submited_month = request.POST.get('month')
            submited_remarks = request.POST.get('remarks')
            print(submited_amount)
            print(submited_room)
            print(submited_month)
            print(submited_remarks)
            return redirect ('add-rent')
        except Exception as e:
            return redirect(request.path)
        