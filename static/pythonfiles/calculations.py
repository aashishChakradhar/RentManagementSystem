from rent.models import *
import json
import os
from decimal import Decimal

month_list = ['Baishak','Jestha','Asar','Shrawan','Bhadra','Ashoj','Kartik','Mangshir','Poush','Magh','Falgun','Chaitra']
month = {
    month_list.index(month_name)+1 : month_name for month_name in month_list
}

def MonthData():
    month_list = ['Baishak','Jestha','Asar','Shrawan','Bhadra','Ashoj','Kartik','Mangshir','Poush','Magh','Falgun','Chaitra']
    month = {
        month_list.index(month_name)+1 : month_name for month_name in month_list
    }
    return month
def YearData():
    year_list = [2081]
    return year_list
def RoomData():
    room_list = ['Grounfloor Front','Groundfloor Back','1. First Floor Front','2. First Floor Back','3. Second Floor Front','4. Second Floor Back','Kitchen']
    room = {
        room_list.index(room_name)+1 : room_name for room_name in room_list
    }
    return room
    

def ensure_directory_exists(path):
    """Ensure the specified directory exists; if not, create it."""
    if not os.path.exists(path):
        os.makedirs(path)

def write_json_to_file(data, filename, path):
    """Write the given data to a JSON file at the specified path."""
    with open(os.path.join(path, filename), 'w') as json_file:
        json.dump(data, json_file, indent=4)

def rooms_to_json(path):
    ensure_directory_exists(path)
    rooms = Room.objects.all()
    mydict = {}
    for room in rooms:
        mydict[room.room_number] = {
            'room_name': room.room_name,
            'rent_amount': str(room.rent_amount),
            'available': room.available,
        }
    write_json_to_file(mydict, 'rooms.json', path)

def payments_to_json(path):
    ensure_directory_exists(path)
    payments = Payment.objects.all()
    pays = {}
    for payment in payments:
        pays[payment.room_no.room_number] = {
            'received_amount': str(payment.recieved_amount),
            'received_month': int(payment.recieved_month),
            'received_year': int(payment.recieved_year),
            'remarks': payment.remarks,
        }
    write_json_to_file(pays, 'payments.json', path)

def remaining_amount_to_json(path):
    ensure_directory_exists(path)
    amounts = RemainingAmount.objects.all()
    amt = {}
    for amount in amounts:
        amt[amount.room_no.room_number] = {
            'amount_remaining': str(amount.amount_remaining),
            'months_remaining': int(amount.months_remaining),
            'remarks': amount.remarks,
        }
    write_json_to_file(amt, 'remaining_amount.json', path)

def individual_to_json(path):
    ensure_directory_exists(path)
    individuals = Individual.objects.all()
    indv = {}
    for individual in individuals:
        indv[individual.room_no.room_number] = {
            'name': str(individual.name),
            'phone': str(individual.phone),
            'is_active': str(individual.is_acitve),
            'remarks': individual.remarks,
            'joining': str(individual.joining),
        }
    write_json_to_file(indv, 'individual.json', path)

def export_to_json():
    export_path = "zJsonBackup"
    rooms_to_json(export_path)
    payments_to_json(export_path)
    remaining_amount_to_json(export_path)
    individual_to_json(export_path)










# def from_json_to_db():
#     with open(rooms.json, 'r') as json_file:
#         data = json.load(json_file)
        
#     for room_number, room_data in data.items():
#         room_number = int(room_number)  # Convert key back to integer if necessary
#         room_name = str(room_data['room_name'])
#         rent_amount = Decimal(room_data['rent_amount'])  # Convert string back to Decimal
#         available = bool(room_data['available'])
        
#         # Create or update the Room object
#         room, created = Room.objects.update_or_create(
#             room_number=room_number,
#             defaults={
#                 'room_name': room_name,
#                 'rent_amount': rent_amount,
#                 'available': available,
#             }
#         )