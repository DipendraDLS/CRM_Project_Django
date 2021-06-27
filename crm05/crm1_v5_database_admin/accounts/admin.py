from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)         #registering the customer model
admin.site.register(Product)            #registering the Product model
admin.site.register(Order)              #registering the Order model