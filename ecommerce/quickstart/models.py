from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100) 
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=200)
    age = models.IntegerField()
    Dob = models.DateField(blank=True,null=True)
    password = models.CharField(max_length=50)

class meta:

    db_table = 'UserLogin'
    


