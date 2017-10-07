from django.contrib import admin
from .models import Invoice, Quantity, Adjustment

admin.site.register(Invoice)
admin.site.register(Quantity)
admin.site.register(Adjustment)