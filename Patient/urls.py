from django.urls import path
from .views import patient_view,patient_,appointment_,patient_appoint,patient_appoint_,discharge_patient,discharge_,pathology_dep,pathology_dep_,pathology_,patient_update_detali,patient_update_detali_,PatientViewModelViewSet,patient_view_,BookApponitmentModelViewSet,PatientUpdateDetailModelViewSet,AppointmentPatientViewSet,p_Appint
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("patient",PatientViewModelViewSet)
router.register("appointment", BookApponitmentModelViewSet)
router.register("updatedetail",PatientUpdateDetailModelViewSet)
router.register("appoint_patient", AppointmentPatientViewSet)
    

urlpatterns = [
    *router.urls,
    
    path('patient_view_',patient_view_),
    path('patient_view', patient_view),
    path('patient_',patient_),
    path('appointment_',appointment_),
    path('patient_appoint',patient_appoint),
    path('patient_appoint_',patient_appoint_),
    path('discharge_patient',discharge_patient),
    path('discharge_',discharge_),
    path('pathology_dep',pathology_dep),
    path('pathology_dep_',pathology_dep_),
    path('pathology_',pathology_),
    path('patient_update_detali',patient_update_detali),
    path('patient_update_detali_',patient_update_detali_),
    path('p_Appint',p_Appint),
    
]