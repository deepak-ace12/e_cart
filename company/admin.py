from django.contrib import admin

from .models import Company, AdminProfile

admin.site.register(Company)
admin.site.register(AdminProfile)
