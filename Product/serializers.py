from rest_framework import serializers
from .models import Hospital,Doctor,NurseInform,HospitalDepartment,HospitalBranch


class HospitalSerializers(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'


class DoctorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'


class NurseInformSerializers(serializers.ModelSerializer):
    class Meta:
        model = NurseInform
        fields = '__all__'

class HospitalDepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = HospitalDepartment
        fields = '__all__'

class HospitalBranchSerializers(serializers.ModelSerializer):
    class Meta:
        model = HospitalBranch
        fields = '__all__'