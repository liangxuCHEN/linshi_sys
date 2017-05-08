#_*_coding:utf-8_*_
from django.contrib import admin
from sysApp.models import MyUser, Product, Material
# Register your models here.

class myUserRateAdmin(admin.ModelAdmin):
    list_display = ('user','telephone','city')
admin.site.register(MyUser,myUserRateAdmin)

class productAdmin(admin.ModelAdmin):
    list_display = ('name','comment','price')
admin.site.register(Product,productAdmin)

class materialAdmin(admin.ModelAdmin):
    list_display = ('name','comment','price')
admin.site.register(Material,materialAdmin)
