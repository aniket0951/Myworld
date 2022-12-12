from django.db.models import Q
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Receptionist,Prescription,ProfilePicture
from .serializers import ReceptionistSerializers,PrescriptionSerializers,ProfilePictureSerializers


@api_view(['POST'])
def receptionist(request):
    name = request.data.get('name')
    phone_no = request.data.get('phone_no')
    email = request.data.get('email')
    address = request.data.get('address')
    user_name = request.data.get('user_name')

    if name and phone_no:
        res = Receptionist.objects.create(name=name,phone_no=phone_no,email=email,
                                        address=address,user_name=user_name)
        serializers = ReceptionistSerializers(res)
        return Response(serializers.data)
    else:
        return Response('place check !')

@api_view(['GET'])
def receptionist_(request):
    ans = Receptionist.objects.all()
    data = ReceptionistSerializers(ans, many=True).data
    return Response(data)


@api_view(['POST'])
def prescription(request):
    symptoms = request.data.get('symptoms')
    patient = request.data.get('patient')
    doctor_no = request.data.get('doctor_no')
    appointment_date = request.data.get('appointment_date')
    prescription_date = request.data.get('prescription_date')
    paid = request.data.get('paid')
    total = request.data.get('total')

    if symptoms and patient:
        res = Prescription.objects.create(symptoms=symptoms,patient=patient,doctor_no=doctor_no,
            appointment_date=appointment_date,prescription_date=prescription_date,
            paid=paid, total=total)
        serializers = PrescriptionSerializers(res)
        return Response(serializers.data)
    else:
        return Response('No match inform !')

@api_view(['GET'])
def prescription_(request):
    ans = Prescription.objects.all()
    data = PrescriptionSerializers(ans, many=True).data
    return Response(data)

@api_view(['POST'])
def profile(request):
    name = request.data.get('name')
    phone_no = request.data.get('phone_no')
    email = request.data.get('email')
    gender = request.data.get('gender')
    age = request.data.get('age')
    blood_group = request.data.get('blood_group')
    medicine = request.data.get('medicine')

    if name and phone_no:
        res = ProfilePicture.objects.create(name=name,phone_no=phone_no,email=email,
                gender=gender,age=age,blood_group=blood_group,medicine=medicine)
        serializers = ProfilePictureSerializers(res)
        return Response(serializers.data)
    else:
        return Response('not profile match !')

@api_view(['GET'])
def profile_(request):
    ans = ProfilePicture.objects.all()
    data =ProfilePictureSerializers(ans, many=True).data
    return Response(data)

def home(request):
    return render(request,'hospi/homebase.html')

def patient(request):
    return render (request, 'hospi/patient_base.html')

def patient_dashboard(request):
    return render (request, 'hospi/patient_dashboard.html')

def adminclick_view(request):
        return render(request,'hospi/adminclick.html')


def doctorclick_view(request):
    return render(request,'hospi/doctorclick.html')
    
        
def patientclick_view(request):
    if request.user.is_authenticated:
    #return HttpResponseRedirect('afterlogin')
        return render(request,'hospi/patientclick.html')


def admin_signup_view(request):
    return render(request,'hospi/adminsignup.html')


def doctor_signup_view(request):
    return render(request,'hospi/doctorsignup.html')


def patient_signup_view(request):
    return render(request,'hospi/patientsignup.html')




