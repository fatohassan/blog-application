from django.db import models

# Create your models here.
class SignUp(models.Model):
    user_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=50)
    confirm_password= models.CharField(max_length=50)

class LogIn(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=50)
