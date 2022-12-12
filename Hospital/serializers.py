from rest_framework import serializers
from .models import Receptionist, Prescription, ProfilePicture

class ReceptionistSerializers(serializers.ModelSerializer):
    class Meta:
        model = Receptionist
        fields = '__all__'

class PrescriptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'


class ProfilePictureSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProfilePicture
        fields = '__all__'

