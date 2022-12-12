from django.contrib import admin
from .models import PatientView,AppointmentPatient,DischrgePatient,PathologyDep,PatientUpdateDetail,BookApponitment


class PatientViewAdmin(admin.ModelAdmin):
    list_display = ('p_id','patient_name','assigned_doctor_name','address','phone_no',
                    'symptoms','admit_date','release_Date','medicine_cost','room_charge',
                    'doctor_free','other_charge','total_bill')


class AppointmentPatientAdmin(admin.ModelAdmin):
    list_display = ('doctor_id','patient_id','doctor_name','patient_name','discription',
                    'appointment_date','date','status')


class DischrgePatientAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','address','symptoms','admin_date','day', 'bill')


class PathologyDepAdmin(admin.ModelAdmin):
    list_display = ('bactoriology','biochemistry','hematology','parasitology','serology','blood_bank','histopathology')


class PatientUpdateDetailAdmin(admin.ModelAdmin):
    list_display = ('condition','medicine','check_up','out_patient_no')

class BookApponitmentAdmin(admin.ModelAdmin):
    list_display = ('name','address','sick','doctor_name')

admin.site.register(PatientView,PatientViewAdmin)
admin.site.register(AppointmentPatient,AppointmentPatientAdmin)
admin.site.register(DischrgePatient,DischrgePatientAdmin)
admin.site.register(PathologyDep,PathologyDepAdmin)
admin.site.register(PatientUpdateDetail,PatientUpdateDetailAdmin)
admin.site.register(BookApponitment,BookApponitmentAdmin)
