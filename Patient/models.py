from django.db import models
from Product.models import MyBaseModel


class PatientView(MyBaseModel):
    p_id = models.IntegerField() 
    patient_name = models.CharField(max_length=255, blank=True, null=False)
    assigned_doctor_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phone_no = models.IntegerField()
    symptoms = models.CharField(max_length=255)
    admit_date = models.DateTimeField(auto_now_add=True)
    release_Date = models.DateTimeField(auto_now_add=True)
    medicine_cost = models.IntegerField()
    room_charge = models.IntegerField() 
    doctor_free = models.IntegerField()
    other_charge = models.IntegerField()
    total_bill = models.IntegerField()


class AppointmentPatient(MyBaseModel):
    doctor_id = models.IntegerField()
    patient_id = models.IntegerField()
    doctor_name = models.CharField(max_length=255, null=False)
    patient_name = models.CharField(max_length=100, blank = True)
    discription = models.CharField(max_length=255,blank=True)
    appointment_date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(max_length=255)


class DischrgePatient(MyBaseModel):
    name = models.CharField(max_length=255)
    mobile = models.IntegerField()
    address = models.CharField(max_length=255)
    symptoms = models.CharField(max_length=100, blank=True)
    admin_date = models.DateTimeField(auto_now_add=True)
    day = models.CharField(max_length=255)
    bill = models.IntegerField()


class PathologyDep(MyBaseModel):
    bactoriology = models.CharField(max_length=100,blank=True)
    biochemistry = models.CharField(max_length=255,blank=True)
    hematology = models.CharField(max_length=255,blank=True)
    parasitology = models.CharField(max_length=255,blank=True)
    serology = models.CharField(max_length=255,null=True)
    blood_bank = models.CharField(max_length=255,null=True)
    histopathology = models.CharField(max_length=255,null=True)


class PatientUpdateDetail(MyBaseModel):
    condition = models.CharField(max_length=255)
    medicine = models.CharField(max_length=255,blank=True)
    check_up = models.IntegerField()
    out_patient_no = models.IntegerField()
    

class BookApponitment(MyBaseModel):
    name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    sick = models.CharField(max_length=100, blank=True)
    doctor_name = models.CharField(max_length=100)
    