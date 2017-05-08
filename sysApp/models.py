#_*_coding:utf-8_*_
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class MyUser(models.Model):
    user= models.OneToOneField(User)
    telephone = models.CharField(u'手机号',max_length=16)
    adress = models.CharField(u'地址',max_length=200, null=True)
    city = models.CharField(u'所在城市',max_length=50, null=True)
    

class Product(models.Model):
    name = models.CharField(u'产品名称',max_length=50)
    comment = models.CharField(u'产品价格',max_length=200, null=True)
    price = models.FloatField(u'描述',null=True)
    pic = models.CharField(u'图片',max_length=200, null=True)


class Material(models.Model):
    name = models.CharField(u'材料名称',max_length=50)
    price = models.FloatField(u'材料价格',null=True)
    comment = models.CharField(u'描述',max_length=200, null=True)
    pic = models.CharField(u'图片',max_length=200, null=True)