import re
from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import PatientView,AppointmentPatient,DischrgePatient,PathologyDep,PatientUpdateDetail,BookApponitment
from .serializers import PatientViewSerializers,AppointmentPatientSerializers,DischrgePatientSerializers,PathologyDepSerializers,PatientUpdateDetailSerializers,BookApponitmentSerializers
import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from utils import custom_viewsets

class PatientViewModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    model = PatientView
    queryset = PatientView.objects.all()
    serializer_class = PatientViewSerializers
    list_success_message = "Patient view list returend success"
    retrieve_sucess_message = "Patient view retrieve returend success" 
    status_code = 200
    response = {
        "status": None,
        "mag": None,
        "data": None
    }
    
    @action(detail=False, methods=['POST'])
    def view_patient(self, request):
        self.response.update({
            "status": 200,
            "mag": 'patient view data view featch',
            "data": {}
        })
        return Response(self.response)


@api_view(['DELETE'])
def patient_view_(request):
    id = request.data.get('id')
    if id is None or id == "":
        return Response('please id')
    PatientView.objects.filter(
        id=id).delete()
    response = {
        "satus": True,
        "mag": 'patient register id delete success',
        "error": 'null',
        "data" : {}
    }
    return Response(response)

@api_view(['POST'])
def patient_view(request):
    p_id = request.data.get('p_id')
    patient_name = request.data.get('patient_name')
    assigned_doctor_name = request.data.get('assigned_doctor_name')
    address = request.data.get('address')
    phone_no = request.data.get('phone_no')
    symptoms = request.data.get('symptoms')
    admit_date = request.data.get('admit_date')
    release_Date = request.data.get('release_Date')
    medicine_cost = request.data.get('room_charge')
    room_charge = request.data.get('room_charge')
    doctor_free = request.data.get('doctor_free')
    other_charge = request.data.get('other_charge')
    total_bill = request.data.get('total_bill')

    if p_id and patient_name and assigned_doctor_name and address and phone_no:
        res = PatientView.objects.create(p_id=p_id,patient_name=patient_name,address=address,
                    assigned_doctor_name=assigned_doctor_name,phone_no=phone_no,symptoms=symptoms,
                    admit_date=admit_date,release_Date=release_Date,medicine_cost=medicine_cost,
                    room_charge=room_charge,doctor_free=doctor_free,other_charge=other_charge,
                    total_bill=total_bill)
        serializers = PatientViewSerializers(res)
        response = {
        "status" : 200 ,
        "msg":"paient data fetch successfully",
        "data" : serializers.data
        }
        return Response(response)
    else:
        return Response('please check the patient !')

@api_view(['GET'])
def patient_(request):
    ans = PatientView.objects.all()
    data = PatientViewSerializers(ans, many=True).data
    return Response(data)

@api_view(['POST'])
def appointment_(request):
    doctor_id = request.data.get('doctor_id')
    patient_id = request.data.get('patient_id')
    doctor_name = request.data.get('doctor_name')
    patient_name = request.data.get('patient_name')
    discription = request.data.get('discription')
    appointment_date = request.data.get('appointment_date')
    date = request.data.get('date')
    status = request.data.get('status')

    if doctor_id and patient_id:
        res = AppointmentPatient.objects.create(doctor_id=doctor_id,patient_id=patient_id,
            doctor_name=doctor_name,patient_name=patient_name,discription=discription,
            appointment_date=appointment_date,date=date,status=status)
        serializers = AppointmentPatientSerializers(res)
        response = {
        "status" : True ,
        "msg":"appointment fetch successfully",
        "data" : serializers.data
        }
        return Response(response)
    else:
        return Response('The appointment letter !')

@api_view(['GET'])
def patient_appoint(request):
    ans = AppointmentPatient.objects.all()
    data = AppointmentPatientSerializers(ans, many=True).data
    
    response = {
        "status" : 200 ,
        "msg":"Appoint fetch successfully",
        "data" : data
    }
    return Response(response)

@api_view(['DELETE'])
def patient_appoint_(request):
    id = request.data.get('id')
    if id is None or id == "":
        return Response('please id')
    AppointmentPatient.objects.filter(
        id=id).delete()
    response = {
        "satus": True,
        "mag": 'patient id delete success',
        "error": 'null',
        "data" : {}
    }
    return Response(response)


@api_view(['POST'])
def discharge_patient(request):
    name = request.data.get('name')
    mobile = request.data.get('mobile')
    address = request.data.get('address')
    symptoms = request.data.get('symptoms')
    admin_date = request.data.get('admin_date')
    day = request.data.get('day')
    bill = request.data.get('bill')

    if name and mobile:
        res = DischrgePatient.objects.create(name=name,mobile=mobile,address=address,
                    symptoms=symptoms,admin_date=admin_date,day=day,bill=bill)
        serializers = DischrgePatientSerializers(res)
        return Response(serializers.data)
    else:
        return Response('No discharge !')

@api_view(['GET'])
def discharge_(request):
    ans = DischrgePatient.objects.all()
    data = DischrgePatientSerializers(ans, many=True).data
    return Response(data)

@api_view(['POST'])
def pathology_dep(request):
    bactoriology = request.data.get('bactoriology')
    biochemistry = request.data.get('biochemistry')
    hematology = request.data.get('hematology')
    parasitology = request.data.get('parasitology')
    serology = request.data.get('serology')
    blood_bank = request.data.get('blood_bank')
    histopathology = request.data.get('histopathology')

    if bactoriology and biochemistry:
        res = PathologyDep.objects.create(bactoriology=bactoriology,biochemistry=biochemistry,
                hematology=hematology,parasitology=parasitology,serology=serology,
                blood_bank=blood_bank,histopathology=histopathology)
        serializers = PathologyDepSerializers(res)
        return Response(serializers.data)
    else:
        return Response('Please check !') 

@api_view(['GET'])
def pathology_dep_(request):
    ans = PathologyDep.objects.all()
    data = PathologyDepSerializers(ans, many=True).data
    return Response(data)


@api_view(['DELETE'])
def pathology_(request):
    id = request.data.get('id')
    if id is  None or id == "":
        return Response("Please provide a required params")
    PathologyDep.objects.filter(
        id=id).delete()
    response = {
        "status" : 200,
        "msg": "id deleted successfully",
        "data" : {}
    }    
    return Response(response)

@api_view(['POST'])
def patient_update_detali(request):
    condition = request.data.get('condition')
    medicine = request.data.get('medicine')
    check_up = request.data.get('check_up')
    out_patient_no = request.data.get('out_patient_no')

    if condition and medicine:
        res = PatientUpdateDetail.objects.create(condition=condition,medicine=medicine,
                        check_up=check_up,out_patient_no=out_patient_no)
        serializers = PatientUpdateDetailSerializers(res)
        return Response(serializers.data)
    else:
        return Response('Please detail patient !')


@api_view(['GET'])
def patient_update_detali_(request):
    ans = PatientUpdateDetail.objects.all()
    data = PatientUpdateDetailSerializers(ans, many=True).data
    return Response(data)


class BookApponitmentModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    model = BookApponitment
    queryset = BookApponitment.objects.all()
    serializer_class = BookApponitmentSerializers
    list_success_message = "book appointment list returend success"
    retrieve_sucess_message = "book appointment retrieve returend success" 
    status_code = 200
    response = {
        "status": None,
        "msg": None,
        "data": None
    }

    @action(detail=False, methods=['POST'])
    def book_appointment(self, request):
        self.response.update({
            "status": True,
            "msg": 'book appointment success',
            "data": {}
        })
        return Response(self.response)


class PatientUpdateDetailModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    model = PatientUpdateDetail
    queryset = PatientUpdateDetail.objects.all()
    serializer_class = PatientUpdateDetailSerializers
    list_success_message ="Patient update detail returend success"
    retrieve_sucess_message = "Patient update detail retrieve returend success"
    status_code = 200
    response = {
        "status": None,
        "msg": None,
        "data": None
    }
    @action(detail= False, methods=['POST'])
    def patient_details(self, request):
        self.response.update({
            "status": 400,
            "msg": 'The patient update detail correct',
            "data": {}
        })
        return Response(self.response)


class AppointmentPatientViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    model = AppointmentPatient
    queryset = AppointmentPatient.objects.all()
    serializer_class = AppointmentPatientSerializers
    list_success_message ="Patient appointment returend success"
    retrieve_sucess_message = "Patient appointment retrieve returend success"
    status_code = 400
    response = {
        "status": None,
        "msg": None,
        "data": None
    }

    @action(detail=False, methods=['PUT'])
    def patient_appoint(self, request):
        self.response.update({
            "status": True,
            "msg": 'The appointment success',
            "data": {}
        })
        return Response(self.response)


@api_view(['DELETE'])
def p_Appint(request):
    id = request.data.get('id')
    if id is None or id =="":
        return Response('Please id')
    AppointmentPatient.objects.filter(
        id=id).delete()
    response = {
        "status": 200,
        "msg": 'id delete success',
        "data": {}
    }
    return Response(response)