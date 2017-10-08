from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Company(models.Model):

    company_name = models.CharField(max_length=100, default='')
    street = models.CharField(max_length=100, default='')
    city = models.CharField(max_length=20, default='')
    state_code = models.CharField(max_length=2, default='')
    zip = models.CharField(max_length=6, default='')
    contact = models.CharField(max_length=10, default='')
    image = models.ImageField(upload_to='company_logo', blank=True, null=True)

    def __str__(self):
        return self.company_name


class AdminProfile(models.Model):
    user = models.OneToOneField(User)
    company = models.ForeignKey(Company, null=True)

    def __str__(self):
        return str(self.user)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = AdminProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


