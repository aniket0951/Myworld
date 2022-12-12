from django.contrib import admin
from .models import Receptionist,Prescription,ProfilePicture

# Register your models here.
class ReceptionistAdmin(admin.ModelAdmin):
    list_display = ('name','phone_no','email','address','user_name')


class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('symptoms','patient','doctor_no','appointment_date','prescription_date',
                        'paid','total')


class ProfilePictureAdmin(admin.ModelAdmin):
    list_display = ('name','phone_no','email','gender','age','blood_group','medicine')


admin.site.register(Receptionist,ReceptionistAdmin)
admin.site.register(Prescription,PrescriptionAdmin)
admin.site.register(ProfilePicture,ProfilePictureAdmin)
