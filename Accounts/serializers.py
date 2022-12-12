from rest_framework import serializers
from .models import PatientPayment,OnlineRegister,PatientLogin


class PatientPaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = PatientPayment
        fields = '__all__'

class OnlineRegisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = OnlineRegister
        fields = '__all__'

class PatientLoginSerializers(serializers.ModelSerializer):
    class Meta:
        model = PatientLogin
        fields = '__all__'