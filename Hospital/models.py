from django.db import models
from Product.models import MyBaseModel
from django.contrib.auth.models import User


class Receptionist(MyBaseModel):
    name = models.CharField(max_length=255,blank=True)
    phone_no = models.IntegerField()
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)


class Prescription(MyBaseModel):
    symptoms = models.CharField(max_length=255,blank=True)
    patient = models.IntegerField()
    doctor_no = models.IntegerField()
    appointment_date = models.DateTimeField(auto_now_add=True)
    prescription_date = models.DateTimeField(auto_now_add=True)
    paid = models.IntegerField()
    total = models.IntegerField()


class ProfilePicture(MyBaseModel):
    name = models.CharField(max_length=255)
    phone_no = models.IntegerField()
    email = models.CharField(max_length=255)
    gender = models.CharField(max_length=100,blank=True)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=100, blank=True)
    medicine = models.IntegerField()


