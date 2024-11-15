from django.shortcuts import render, redirect,HttpResponse
from django.views import View
from django.urls import reverse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

from rent.models import *
from static.pythonfiles.calculations import *

from django.http import JsonResponse

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
            submited_month = request.POST.get('date')
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
            payment = Payment.objects.create(
                room_no = room_no,
                recieved_amount = submited_amount,
                recieved_month = submited_month,
                recieved_year = submited_year,
                remarks = submited_remarks)
            payment.save()
            messages.success(request, "Entry Successful")
        except Exception as e:
            messages.error(request, "Select Valid Options")
            return redirect(request.path)
        try:
            create_backup()
        except Exception as e:
            messages.error(request, "Backup Creation Fail")
            return redirect(request.path)
        
        return redirect('rent:add-rent')
          
class ViewRentHistory(BaseView):
    def get(self,request):
        try:
            # restore_backup()
            rooms = Room.objects.all()
        except Exception as e:
            messages.error(request,str(e))
            return redirect (request.path)
        
        submited_room = request.session.get('submited_room', [])
        submited_month = request.session.get('submited_month', [])
        if submited_room and submited_month:
            del request.session['submited_room']
            del request.session['submited_month']
            
        
        histories = []
        if submited_room and submited_month:
            try:
                # Fetch the room details based on the submitted room ID
                room = Room.objects.filter(uid=submited_room).first()
                if room:
                    histories = Payment.objects.filter(room_no=room.uid)
            except Exception as e:
                messages.error(request, str(e))    
                return redirect(request.path)
        
        context = {
            "app_name": "myRent",
            "page_name": "view-rent",
            "months": MonthData(),
            "rooms": rooms,
            "histories": histories,
        }
        return render(request,'view_rent.html',context)
    
    def post (self,request):
        try:
            submited_room = request.POST.get('room')
            submited_month = int(request.POST.get('month'))
            if not submited_room or not submited_month:
                raise ValueError("Room and Month are required.")
        except Exception as e:
            messages.error(request,"Room and Month are required.")
            return redirect(request.path)
        
        try:
            request.session['submited_room'] = submited_room
            request.session['submited_month'] = submited_month
            return redirect('rent:view-rent')
        except Exception as e:
            messages.error(request,str(e))
            return redirect(request.path)

class BackupAction(BaseView):
    def get(self, request):
        context = {
            'page_name' : 'backup-action',
            'app_name' : 'myRent',
        }
        return render(request,'exportdatabase.html',context)
    def post(self, request):
        try:
            operation = request.POST.get('action')
        except Exception as e:
            messages.error(request,str(e))
            return redirect(request.path)
        
        if operation == 'restore':
            try:
                restore_backup()
                messages.success(request,f"Backup Restored Successfully")
                return redirect('rent:backup-action')
            except Exception as e:
                messages.error(request,str(e))
                return redirect(request.path)
        elif operation == 'backup':
            try:
                create_backup()
                messages.success(request,f"Backup Created Successfully")
                return redirect('rent:backup-action')
            except Exception as e:
                messages.error(request,str(e))
                return redirect(request.path)
        elif operation == None:
            try:
                messages.error(request,f"Select a valid action")
                return redirect('rent:backup-action')
            except Exception as e:
                messages.error(request,str(e))
                return redirect(request.path)
            
        
