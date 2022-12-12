from django.urls import path
from .views import  PatientPaymentModelViewSet,OnlineRegisterModelViewSet,PatientLoginModelViewSet,patient_register,p_login

from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("payments", PatientPaymentModelViewSet)
router.register("onlineRegister",OnlineRegisterModelViewSet )
router.register("patientlogin",PatientLoginModelViewSet)

urlpatterns = [
    path('patient_register',patient_register),
    path('p_login',p_login),

    *router.urls
]