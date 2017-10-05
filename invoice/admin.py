from django.contrib import admin
from .models import Invoice, Quantity

admin.site.register(Invoice)
admin.site.register(Quantity)