from django.shortcuts import render, redirect,HttpResponse,get_object_or_404
from django.views import View
from django.urls import reverse

from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

from rent.models import *
from static.pythonfiles.calculations import *

from django.http import JsonResponse

# for nepali date time
import datetime
import nepali

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
        return render(request,'rent_add.html',context)
    
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

class SelectBuilding(View):
    def get(self, request):
        if Building.objects.exists():
            buildings = Building.objects.all()
            context = {
                "page_name": "select-building",
                "app_name": "myRent",
                'buildings': buildings,
            }
            return render(request, 'building_select.html', context)
        else:
            return redirect('rent:add-building')

    def post(self, request):
        building_name = request.POST.get("building_name")
        action = request.POST.get('action')
        if action.lower() == 'add':
            return redirect('rent:add-building')
        elif action.lower() == 'update':
            return redirect('rent:update-building', building_name=building_name)
        elif action.lower() == 'delete':
            return redirect('rent:delete-building', building_name=building_name)        

class AddBuilding(BaseView):
    def get(self,request):
        action = 'add'
        context = {
            "page_name":"add-building",
            "app_name":"myRent",  
            "action":action,
        }
        return render(request,'building_action.html',context)
    
    def post(self,request):
        try:
            building_name = request.POST.get('building_name')
            building_address = request.POST.get('building_address')
            room_count = request.POST.get('room_count')
            building_type = request.POST.get('building_type')
            remarks = request.POST.get('remarks')
            building = Building.objects.create(
                building_name=building_name,
                building_address=building_address,
                building_type=building_type,
                number_of_rooms=room_count,
                is_active=True,
                remarks = remarks
            )
            for room in range(1,int(room_count)+1):
                Room.objects.create(
                    building = building,
                    room_number = room,
                    room_name = f"Room {room}",
                    rent_amount = 0,
                    is_available = True,
                )
            messages.success(request,"Building added successfully")
            return redirect('rent:add-room', building_name = building.uid)
        except Exception as e:
            messages.error(request,f"An error occured: {e}")
            return redirect('rent:add-building')

class UpdateBuilding(BaseView):
    def get(self, request, building_name):
        building = get_object_or_404(Building, uid=building_name)
        action = "update"
        context = {
            "page_name": "update-building",
            "app_name": "myRent",
            "building": building,
            "action": action,
        }
        return render(request, 'building_action.html', context)

    def post(self, request, building_name):
        if 'cancel' in request.POST:
            return redirect('rent:select-building')
        elif 'update' in request.POST:
            building = get_object_or_404(Building, uid=building_name)
            building.building_name = request.POST.get('building_name')
            building.building_address = request.POST.get('building_address')
            building.number_of_rooms = request.POST.get('room_count')
            building.building_type = request.POST.get('building_type')
            building.remarks = request.POST.get('remarks')
            building.save()
            
            messages.success(request, "Building has been updated successfully")
            return redirect('rent:home')

class DeleteBuilding(BaseView):
    def get(self, request, building_name):
        building = get_object_or_404(Building, uid=building_name)
        action = "delete"
        context = {
            "page_name": "update-building",
            "app_name": "myRent",
            "building": building,
            "action": action,
        }
        return render(request, 'building_action.html', context)

    def post(self, request, building_name):
        if 'cancel' in request.POST:
            return redirect('rent:select-building')
        elif 'delete' in request.POST:
            building = get_object_or_404(Building, uid=building_name)
            building.delete()
            messages.success(request, "Building has be removed successfully")
            return redirect('rent:home')        

class AddRoom(BaseView):
    def get(self,request, building_name):
        rooms = Room.objects.filter(building = building_name)
        context = {
            "rooms" : rooms,
            "building": building_name,
            "page_name":"add-room",
        }
        return render(request,"room_add.html",context)
    
    def post(self,request,building_name):
        room_number = request.POST.getlist('room_number')
        room_name = request.POST.getlist('room_name')
        rent = request.POST.getlist('room_rent')
        is_available = request.POST.getlist('availability')
        if len(room_number) == len(room_name) == len(room_number) == len(rent) == len(is_available):
            try:
                building = Building.objects.get(uid=building_name)
                for room_number, room_name, rent,is_available in zip(room_number, room_name, rent, is_available):
                    Room.objects.update_or_create(
                        building = building,
                        room_number = room_number,#unique identifier
                        defaults = {
                            "room_name" : room_name,
                            "rent_amount" : rent,
                            "is_available" : is_available.lower() == 'true'
                        }
                    )
                messages.success(request,f"Rooms Added Successfully.")
                return redirect('rent:home')
            except Exception as e:
                messages.error(request,f"An error occured: {e}")
                return redirect('rent:add-room',building_name = building_name)

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
            
        
