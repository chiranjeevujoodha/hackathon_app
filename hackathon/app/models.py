from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

# class UserAccountManager(BaseUserManager):
    # def create_user(self, email, name, password=None):
    #     if not email:
    #         raise ValueError('Email invalid')

    #     email = self.normalize_email(email)
    #     user = self.model(email=email, name=name)

    #     user.set_password(password)
    #     user.save()

    #     return user

# class UserAccount(AbstractBaseUser,PermissionsMixin):
#     email = models.EmailField(max_lengh=255, unique=True)
#     name = models.CharField(max_lenght=255)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=True)

#     objects = UserAccountManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['name']

#     def get_full_name(self):
#         return self.name
    
#     def get_short_name(self):
#         return self.name
    
#     def __str__(self):
#         return self.email

class NGO(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

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