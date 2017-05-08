from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class MyUser(models.Model):
    user= models.OneToOneField(User)
    telephone = models.CharField(max_length=16)
    adress = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    

class Product(models.Model):
    name = models.CharField(max_length=50)
    comment = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    pic = models.CharField(max_length=200, null=True)


class Material(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField(null=True)
    comment = models.CharField(max_length=200, null=True)
    pic = models.CharField(max_length=200, null=True)