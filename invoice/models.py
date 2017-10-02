from django.db import models
from company.models import Company
from project.models import Project
from project.models import Item
from django.contrib.auth.models import User


class Invoice(models.Model):
    customer = models.ForeignKey(User)
    company = models.ForeignKey(Company, null=True)
    project = models.ForeignKey(Project, null=True)
    items = models.ManyToManyField(Item)
    submitted = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    cart = models.ManyToManyField(Item, related_name='cart')

    @classmethod
    def add_to_cart(cls, current_item):
        project_cart, created = cls.objects.get_or_create(
            project=current_item.project
        )
        project_cart.cart.add(current_item)

    @classmethod
    def remove_from_cart(cls, current_item):
        project_cart, created = cls.objects.get_or_create(
            project=current_item.project
        )
        project_cart.cart.remove(current_item)


