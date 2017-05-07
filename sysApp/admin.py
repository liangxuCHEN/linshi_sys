from django.contrib import admin
from sysApp.models import MyUser, Product, Material
# Register your models here.
admin.site.register(MyUser)
admin.site.register(Product)
admin.site.register(Material)
