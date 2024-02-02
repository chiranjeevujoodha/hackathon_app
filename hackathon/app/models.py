from django.db import models

# Create your models here.


class Campaign(models.Model):
    name = models.CharField(max_length=200)
    organisor = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    date = models.DateField()
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.fname, self.lname