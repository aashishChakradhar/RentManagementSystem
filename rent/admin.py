from django.contrib import admin
from rent.models import *
# Register your models here.

admin.site.register(Room)
admin.site.register(Payment)
admin.site.register(RemainingAmount)
admin.site.register(Individual)