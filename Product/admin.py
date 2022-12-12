from django.contrib import admin
from .models import Hospital,Doctor,NurseInform,HospitalDepartment, HospitalBranch


# Register your models here.
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address1','address2','city','state','country')


class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','address','mobile','department','status','salary','age','gender')


class NurseInformAdmin(admin.ModelAdmin):
    list_display = ('name','address','educations','DOB','girls','boys')

class HospitalDepartmentAdmin(admin.ModelAdmin):
    list_display = ('outpatient_dep','inpatient_service','medical_dep','nursing_dep',
                    'paramedical','operation_theatre_complex','pharmacy','radiology_dep',
                    'non_professional_services','medical_record_dep','personnel_dep')


class HospitalBranchAdmin(admin.ModelAdmin):
    list_display = ('h_name','h_city','no_doctor_present','no_nurse','h_ward','email','password_code')

admin.site.register(Hospital,HospitalAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(NurseInform,NurseInformAdmin)
admin.site.register(HospitalDepartment,HospitalDepartmentAdmin)
admin.site.register(HospitalBranch,HospitalBranchAdmin)