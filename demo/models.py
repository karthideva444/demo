from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    roll = models.IntegerField(unique=True)
    city = models.CharField(max_length=40)
    
    class meta:

        tb_table = "demo_crud"
