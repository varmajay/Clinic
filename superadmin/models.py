from pyexpat import model
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



class Slot(models.Model):
    TIMESLOT_LIST = (
        (0, '09:00 am To 10:00 am'),
        (1, '10:00 am TO 11:00 am'),
        (2, '11:00 am To 12:00 am'),
        (3, '12:00 am To 01:00 pm'),
        (4, '02:00 pm To 03:00 pm'),
        (5, '03:00 pm To 04:00 pm'),
        (6, '04:00 pm To 05:00 pm'),
    )
    WEEKS = (
        (0,'Monday'),
        (1,'Tuesday'),
        (2,'Wednesday'),
        (3,'Thursday'),
        (4,'Friday'),
        (5,'Saturday'),
        (6,'Sunday'),
    )
    doctor_id = models.ForeignKey(User,on_delete=models.CASCADE)
    weeks  = models.IntegerField(choices=WEEKS)
    timeslot = models.IntegerField(choices=TIMESLOT_LIST)


    def __int__(self):
        return self.doctor_id +"@"+self.timeslot

class Appoinment(models.Model):
    STATUS = (
        (0,'Pending'),
        (1,'Completed'),
        (2,'Absent'),
        (3,'Canceled'),
    ) 
    slot = models.ForeignKey(Slot,on_delete=models.CASCADE)
    patients_id = models.IntegerField()
    patient_name = models.CharField(max_length=30)
    weeks = models.IntegerField()
    timeslot = models.IntegerField()
    description = models.TextField( default=None)
    status = models.IntegerField(default=0,choices=STATUS)

    def __int__(self):
        return self.patients_id

    def __str__(self):
        return self.patient_name