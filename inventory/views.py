from django.shortcuts import render,HttpResponse
from datetime import datetime
from inventory.models import Contact
# Create your views here.
def home(request):
    return render (request,'home.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        contact = Contact(fname = fname, lname = lname, email = email, phone=phone, comment = comment, date = datetime.today())
        contact.save()
    return render (request,'contact.html')