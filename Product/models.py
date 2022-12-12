from tabnanny import verbose
from django.db import models


class MyBaseModel(models.Model):
    id = models.AutoField(primary_key = True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)


class Hospital(MyBaseModel):
    name = models.CharField(max_length=255, blank=True)
    address1 = models.CharField(max_length=255, blank=True)
    address2 = models.CharField(max_length=255)
    city = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=100)

    verbose_name = 'Hospitals'
    verbose_name_plural = 'Hospital'


class Doctor(MyBaseModel):
    name = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255)
    mobile = models.IntegerField()
    department = models.CharField(max_length=255)
    status = models.BooleanField(max_length=255)
    salary = models.IntegerField()
    age = models.IntegerField()
    gender = models.CharField(max_length=100)


class NurseInform(MyBaseModel):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    educations = models.CharField(max_length=255)
    DOB = models.DateTimeField(auto_now_add=True)
    girls = models.IntegerField()
    boys = models.IntegerField()
    

class HospitalDepartment(MyBaseModel):
    outpatient_dep = models.IntegerField()
    inpatient_service = models.IntegerField()
    medical_dep = models.IntegerField()
    nursing_dep = models.IntegerField()
    paramedical = models.IntegerField()
    operation_theatre_complex = models.IntegerField()
    pharmacy = models.IntegerField()
    radiology_dep = models.IntegerField()
    non_professional_services = models.IntegerField()
    medical_record_dep = models.IntegerField()
    personnel_dep = models.IntegerField()



class HospitalBranch(MyBaseModel):
    h_name = models.CharField(max_length=255)
    h_city = models.CharField(max_length=255, blank=True)
    no_doctor_present = models.IntegerField()
    no_nurse = models.IntegerField()
    h_ward = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    password_code = models.IntegerField()