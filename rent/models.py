from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import random
import uuid

# Create your models here.

class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    class Meta:
        abstract=True

class Room(BaseModel):
    room_number = models.IntegerField(default=1)
    room_name = models.CharField(max_length=15, default='Room')
    rent_amount = models.DecimalField(decimal_places=2,max_digits=4, default=3000.00)
    available = models.BooleanField(default=True)
    def __str__(self):
        return self.room_name

class PaymentHistories(BaseModel):
    room_no = models.ForeignKey(Room, related_name='Room_History', on_delete=models.CASCADE)
    recieved_amount = models.DecimalField(decimal_places=0,max_digits=4,default=0.00)
    recieved_month = models.IntegerField(default=1)
    recieved_year = models.IntegerField(default=2081)
    amount_remaining = models.DecimalField(decimal_places=2, max_digits=4,default=0.00)
    months_remaining = models.IntegerField(default=0)
    remarks = models.TextField(default=None)
    def __str__(self):
        return self.room

class RemainingAmount(BaseModel):
    room_no = models.ForeignKey(Room, related_name='Room_Calculation', on_delete=models.CASCADE)
    amount_remaining = models.DecimalField(decimal_places=2, max_digits=4,default=0.00)
    months_remaining = models.IntegerField(default=0)
    remarks = models.TextField(default=None)
    def __str__(self):
        return self.room
    
class Individual(BaseModel):
    room_no = models.ForeignKey(Room, related_name='Room_Individual', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default='Unknown')
    phone = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    
    joining = models.DateField()
    