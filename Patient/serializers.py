from rest_framework import serializers
from .models import PatientView,AppointmentPatient,DischrgePatient,PathologyDep,PatientUpdateDetail,BookApponitment


class PatientViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = PatientView
        fields = '__all__'


class AppointmentPatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = AppointmentPatient
        fields = '__all__'


class DischrgePatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = DischrgePatient
        fields = '__all__'

class PathologyDepSerializers(serializers.ModelSerializer):
    class Meta:
        model = PathologyDep
        fields = '__all__'


class PatientUpdateDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = PatientUpdateDetail
        fields = '__all__'

class BookApponitmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = BookApponitment
        fields = '__all__'