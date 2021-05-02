from django.contrib import admin

# Register your models here.
from .models import Chamber, ChamberType, Client, Reservation, OnlineRequest,Invoice, Employee
admin.site.register(Client)
admin.site.register(Employee)
admin.site.register(Chamber)
admin.site.register(ChamberType)
admin.site.register(Reservation)
admin.site.register(OnlineRequest)
admin.site.register(Invoice)
