from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default = 'test@test.com')

    def __str__(self):
        return self.name


class Campaign(models.Model):
    name = models.CharField(max_length=200)
    organisor = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    location = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, {self.organisor}, {self.author}'
    
    
class Contact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.fname} {self.lname}'
    

class Profile(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50)
    about_desc = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
