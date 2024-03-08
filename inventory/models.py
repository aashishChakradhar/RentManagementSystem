from django.db import models

# Create your models here.

class Contact(models.Model):
    fname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=50)
    comment = models.TextField()
    date = models.DateField()