from random import choices
from django.db import models
from django.forms import CharField

# Create your models here.


class User(models.Model):
    GENDER_MALE = 0
    GENDER_FEMALE = 1
    GENDER_CHOICES = ((GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'))
    ROLES = (

        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patients', 'Patients'),

    )


    roles = models.CharField(max_length=30,choices = ROLES)

    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    clinic_name = models.CharField(max_length=30,default=None,blank=True,null=True)
    gender = models.IntegerField(choices=GENDER_CHOICES,default=None,null=True,blank=True)
    specialty = models.CharField(max_length=30,default=None,blank=True,null=True)
    address = models.TextField(default=None,blank=True,null=True)
    profile = models.FileField(upload_to='user',default='profile.png')
    

    def __sts__(self):
        return self.name+" "+self.email