from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):

    company_name = models.CharField(max_length=100, default='')
    street = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=20, default='')
    state_code = models.CharField(max_length=5, default='')
    contact = models.CharField(max_length=10, default='')
    image = models.ImageField(upload_to='company_logo', blank=True, null=True)

    def __str__(self):
        return self.company_name


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    company_name = models.ForeignKey(Company, null=True)


