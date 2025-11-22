from django.db import models
from django.contrib import admin
class Car(models.Model):
    brand_name=models.CharField(max_length=20)
    car_name=models.CharField(max_length=20)
    engi_num=models.IntegerField()
    release_date=models.DateField()

class CarAdmin(admin.ModelAdmin):
    list_display=('brand_name', 'car_name', 'engi_num', 'release_date')
# Create your models here.
