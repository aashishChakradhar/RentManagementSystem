from django.db import models
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import random
import uuid

# Create your models here.

class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)
    class Meta:
        abstract=True

class Building(BaseModel):
    building_name = models.CharField(max_length=50,unique=True)
    building_address = models.TextField()
    number_of_rooms = models.IntegerField()
    building_type = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)
    remarks = models.TextField(default='None')

    def __str__(self):
        return f'{self.building_name} in {self.building_address}'

class Room(BaseModel):
    building = models.ForeignKey(Building, on_delete=models.CASCADE)
    room_number = models.IntegerField(default=1)
    room_name = models.CharField(max_length=30)
    rent_amount = models.DecimalField(decimal_places=2,max_digits=6, default=3000.00)
    is_available = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.room_number} - {self.room_name}"

    class Meta:
        ordering = ['room_number']  # Order rooms by their number

class Payment(BaseModel):
    room_no = models.ForeignKey(Room, related_name='room_history', on_delete=models.CASCADE)
    received_amount = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    date = models.DateField()
    remarks = models.TextField(null=True, blank=True)
    
    # class Meta:
    #     ordering = ['created_at']
    #     unique_together = ('room_no', 'received_month', 'received_year')  # Prevent duplicate payments for the same period

    def __str__(self):
        return (
            f"Room {self.room_no.room_number} - {self.room_no.room_name} | "
            f"Amount: {self.received_amount} | Date: {self.date}"
        )

class RemainingAmount(BaseModel):
    room_no = models.ForeignKey(Room, related_name='Room_Calculation', on_delete=models.CASCADE)
    amount_remaining = models.DecimalField(decimal_places=2, max_digits=6,default=0.00)
    months_remaining = models.IntegerField(default=0)
    remarks = models.TextField(default=None)
    
class Individual(BaseModel):
    room_no = models.ForeignKey(Room, related_name='Room_Individual', on_delete=models.CASCADE)
    name = models.CharField(max_length=30, default='Unknown')
    phone = models.DecimalField(max_digits=10,decimal_places=0,default=0)
    is_acitve = models.BooleanField( default = True)
    remarks = models.TextField(default = 'none')
    joining = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.room_no.room_number}-{self.name}'
    
    class Meta:
        ordering = ['room_no__room_number']