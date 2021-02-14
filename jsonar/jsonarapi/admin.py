from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Customers)
admin.site.register(Payment)
admin.site.register(Rentals)
admin.site.register(Films)
admin.site.register(Actors)
admin.site.register(Staff)

