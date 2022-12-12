from django.urls import path
from Hospital import views
from .views import receptionist,receptionist_,prescription,prescription_,profile,profile_
from .views import doctorclick_view,home,patient,patient_dashboard,doctorclick_view


urlpatterns = [
    path('',home,name='home'),
    path('patiens',patient,name='patient'),
    path('patient_dashboard',patient_dashboard, name='patient_dashboard'),
    path('doctorclick_view',doctorclick_view,name='doctorclick_view'),
    path('doctorclick_view',doctorclick_view,name='doctorclick_view'),
    

    path('receptionist',receptionist),
    path('receptionist_',receptionist_),
    path('prescription',prescription),
    path('prescription_',prescription_),
    path('profile',profile),
    path('profile_',profile_),
    
   
]