from django.db import models
from Product.models import MyBaseModel

# Create your models here.
class PatientPayment(MyBaseModel):
    p_name = models.CharField(max_length=255, blank=True)
    p_address = models.CharField(max_length=255, blank=True)
    medicine_cost = models.IntegerField()
    room_charge = models.IntegerField()
    doctor_free = models.IntegerField()
    other_charge = models.IntegerField()
    total_bill = models.IntegerField()


class OnlineRegister(MyBaseModel):
    name =models.CharField(max_length=255, blank=True)
    address =models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255, blank=True)
    phone_no = models.IntegerField()
    sick = models.CharField(max_length=255, blank=True)
    no = models.IntegerField()

class PatientLogin(MyBaseModel):
    p_name = models.CharField(max_length=255, blank=True)
    doctor_name = models.CharField(max_length=255)
    sick = models.CharField(max_length=100, blank=True)
    appoint_date = models.DateTimeField(auto_now_add=True)

