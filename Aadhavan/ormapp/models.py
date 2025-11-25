from django.db import models
from django.contrib import admin

class Ecommerce(models.Model):
    Product_Name=models.CharField(max_length=100)
    Product_Price=models.FloatField()
    Product_Manufacturer=models.CharField(max_length=30)
    Product_Brand_Name=models.CharField(max_length=20)
    Product_Id=models.IntegerField(primary_key=True)
    Product_Quantity=models.IntegerField()
    Product_Manufactured_Date=models.DateField()

class Admin(admin.ModelAdmin):
    list_display=["Product_Name","Product_Price","Product_Manufacturer","Product_Brand_Name","Product_Id","Product_Quantity","Product_Manufactured_Date"]
    actions_on_top=True

