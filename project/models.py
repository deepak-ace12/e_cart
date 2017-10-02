from django.db import models
from company.models import Company


class Item(models.Model):
    item_name = models.CharField(max_length=20, default='')
    unit_price = models.IntegerField(default=0)
    project = models.ForeignKey('Project', blank=True, related_name='project', null=True)
    image = models.ImageField(upload_to='product_image', blank=True, null=True)

    def __str__(self):
        return self.item_name


class Project(models.Model):
    project_name = models.CharField(max_length=20, default='')
    company = models.ForeignKey(Company)
    products = models.ManyToManyField(Item, related_name='item')

    def __str__(self):
        return self.project_name




