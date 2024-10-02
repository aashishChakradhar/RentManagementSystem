from django.shortcuts import render, redirect,HttpResponse
from django.views import View

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

from rent.models import *
from static.pythonfiles.calender import *
# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
class BaseView(LoginRequiredMixin, View): #to check login or not
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
            return redirect('/')
        else:
            messages.error(request, "You should check in on some of those fields below.")
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
        try: 
            rooms = Room.objects.all()
        except Exception as e:
            messages.error(request, str(e))
            return redirect(request.path)
        
        context = {
            "page_name":"add-rent",
            "app_name":"myRent",
            "months" : MonthData(),
            "years" : YearData(),
            "rooms": rooms,   
        }
        return render(request,'add_rent.html',context)
    
    def post (self,request):
        try:
            submited_room = request.POST.get('room')
            submited_amount = request.POST.get('amount')
            submited_year = request.POST.get('year')
            submited_month = request.POST.get('month')
            submited_remarks = request.POST.get('remarks')
        except Exception as e:
            messages.error(request, str(e))
            return redirect(request.path)
        
        try:
            room_no = Room.objects.filter(uid=submited_room).first()
            if not room_no:
                messages.error(request, "Room not found")
                return redirect(request.path)
        except Exception as e:
            messages.error(request, str(e))
            return redirect(request.path)
        
        try:
            payment = PaymentHistories.objects.create(
                room_no = room_no,
                recieved_amount = submited_amount,
                recieved_month = submited_month,
                recieved_year = submited_year,
                remarks = submited_remarks)
            payment.save()
            messages.success(request, "Entry Successful")
            return redirect('rent:add-rent')
        
        except Exception as e:
            messages.error(request, str(e))
            return redirect(request.path)
        
        
        
class ViewRent(BaseView):
    def get(self,request):
        submited_room = request.session.get('submited_room', [])
        submited_month = request.session.get('submited_month', [])
        if submited_room and submited_month:
            del request.session['submited_room']
            del request.session['submited_month']
        details = zip(submited_room, submited_month)
        
        context = {
            "app_name": "myRent",
            "page_name": "view-rent",
            "months": MonthData(),
            "rooms": RoomData(),
            "details": details,
        }
        
        return render(request,'view_rent.html',context)
    
    def post (self,request):
        try:
            submited_room = int(request.POST.get('room'))
            submited_month = int(request.POST.get('month'))
            print(submited_room)
            print(submited_month)
           
            room = [x for x in range(submited_room * 10)]
            month = [x for x in range(submited_month * 10)]
            request.session['submited_room'] = room
            request.session['submited_month'] = month
            return redirect(request.path)
            
        except Exception as e:
            print(e)
            return redirect(request.path)
        