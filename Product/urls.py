from django.urls import path
from .views import hospital_inform,hospital_,hospital,doctor_,doctor_inform,nurse_inform,nurse_inform_ge,hospital_depart,department_,department,DoctorModeViewSet,d_inform,HospitalModelViewSet,HospitalBranchModelViewSet,h_branch
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("doctor", DoctorModeViewSet),
router.register("hospital", HospitalModelViewSet),
router.register("branch", HospitalBranchModelViewSet),

urlpatterns = [
    *router.urls,
    
    path('hospital_inform',hospital_inform),
    path('hospital_',hospital_),
    path('hospital',hospital),
    path('doctor_',doctor_),
    path('doctor_inform',doctor_inform),
    path('nurse_inform',nurse_inform),
    path('nurse_inform_ge',nurse_inform_ge),
    path('hospital_depart',hospital_depart),
    path('department_',department_),
    path('department',department),
    path('d_inform',d_inform), 
    path('h_branch',h_branch),

]