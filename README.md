# Ex01 Django ORM Web Application
## Date: 22.11.2025

## AIM
To develop a Django Application to store and retrieve data from a E-Commerce Website Database for Amazon or Flipkart using Object Relational Mapping(ORM).



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from .models import Ecommerce,Admin
admin.site.register(Ecommerce,Admin)

```




## OUTPUT
![alt text](<Screenshot (64).png>)



## RESULT
Thus the program for creating E-commerce website database using ORM hass been executed successfully
