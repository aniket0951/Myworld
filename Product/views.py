from audioop import add
from django.shortcuts import render
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .models import Hospital,Doctor,NurseInform, HospitalDepartment,HospitalBranch
from .serializers import HospitalSerializers,DoctorSerializers,NurseInformSerializers,HospitalDepartmentSerializers,HospitalBranchSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, AllowAny
from utils import custom_viewsets


@api_view(['POST'])
def hospital_inform(request):
    name = request.data.get('name')
    address1 = request.data.get('address1')
    address2 = request.data.get('address2')
    city = request.data.get('city')
    state = request.data.get('state')
    country = request.data.get('country')

    if name and address1:
        res = Hospital.objects.create(name=name,address1=address1,address2=address2,
                        city=city,country=country,state=state)
        serializers = HospitalSerializers(res)
        return Response(serializers.data)
    else:
        return Response('No hospital match !')

@api_view(['GET'])
def hospital_(request):
    ans = Hospital.objects.all()
    data = HospitalSerializers(ans, many=True).data
    return Response(data)

@api_view(['DELETE'])
def hospital(request):
    id = Hospital.objects.filter(id= request.data.get('id')).delete()
    return Response('Successfull !')


@api_view(['POST'])
def doctor_(request):
    name = request.data.get('name')
    address = request.data.get('address')
    mobile = request.data.get('mobile')
    department = request.data.get('department')
    status =request.data.get('status')
    salary = request.data.get('salary')
    age = request.data.get('age')
    gender = request.data.get('gender')

    if name and address and mobile:
        ans = Doctor.objects.create(name=name, address=address,mobile=mobile,department=department,
                            status=status,salary=salary,age=age,gender=gender)
        serializers = DoctorSerializers(ans)
        return Response(serializers.data)
    else:
        return Response('plase wait the doctor !')

@api_view(['GET'])
def doctor_inform(request):
    res = Doctor.objects.all()
    data = DoctorSerializers(res, many=True).data
    return Response(data)

@api_view(['POST'])
def nurse_inform(request):
    name = request.data.get('name')
    address = request.data.get('address')
    educations = request.data.get('educations')
    DOB = request.data.get('DOB')
    girls = request.data.get('girls')
    boys = request.data.get('boys')

    if name and address:
        res = NurseInform.objects.create(name=name,address=address,educations=educations,
                                        DOB=DOB,girls=girls,boys=boys)
        serializers = NurseInformSerializers(res)
        return Response(serializers.data)
    else:
        return Response('Please No nurse ! ')

@api_view(['GET'])
def nurse_inform_ge(request):
    ans = NurseInform.objects.all()
    data = NurseInformSerializers(ans, many=True).data
    return Response(data)


@api_view(['POST'])
def hospital_depart(request):
    outpatient_dep = request.data.get('outpatient_dep')
    inpatient_service = request.data.get('inpatient_service')
    medical_dep = request.data.get('medical_dep')
    nursing_dep = request.data.get('nursing_dep')
    paramedical = request.data.get('paramedical')
    operation_theatre_complex = request.data.get('operation_theatre_complex')
    pharmacy = request.data.get('pharmacy')
    radiology_dep = request.data.get('radiology_dep')
    non_professional_services = request.data.get('non_professional_services')
    medical_record_dep = request.data.get('medical_record_dep')
    personnel_dep = request.data.get('personnel_dep')
    

    if outpatient_dep and inpatient_service and medical_dep:
        res = HospitalDepartment.objects.create(outpatient_dep=outpatient_dep,inpatient_service=inpatient_service,
                        medical_dep=medical_dep,nursing_dep=nursing_dep,paramedical=paramedical,
                        operation_theatre_complex=operation_theatre_complex,pharmacy=pharmacy,
                        radiology_dep=radiology_dep,non_professional_services=non_professional_services,
                        medical_record_dep=medical_record_dep,personnel_dep=personnel_dep)
        serializers = HospitalDepartmentSerializers(res)
        return Response(serializers.data)
    else:
        return Response('Please check the depart inform !')

@api_view(['GET'])
def department_(request):
    ans = HospitalDepartment.objects.all()
    data = HospitalDepartmentSerializers(ans, many=True).data
    return Response(data)

@api_view(['DELETE'])
def department(request):
    id = HospitalDepartment.objects.filter(
        id = request.data.get('id')
    ).delete()
    return Response('successfull !')


class DoctorModeViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    model = Doctor
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers
    list_success_message ="Doctor inform returend success"
    retrieve_sucess_message = "Doctor inform retrieve returend success"
    create_success_message = "Doctor is the create"
    status_code = True
    response = {
        "status": None,
        "msg": None,
        "data": None
    }
    
    @action(detail=False, methods=['POST'])
    def d_inform(self, request):
        self.response.update({
            "status": 400,
            "msg": 'doctor inform success',
            "error": 'Null',
            "data" : {}
        })
        return Response(self.response)

@api_view(['DELETE'])
def d_inform(request):
    id = request.data.get('id')
    if id is None or id == "":
        return Response('doctor please id')
    Doctor.objects.filter(
        id= id).delete()
    response = {
        "status": True,
        "msg": 'doctor id delete success',
        "data": {}
    }
    return Response(response)


class HospitalModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    model = Hospital
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializers
    list_success_message ="Hospital inform returend success"
    retrieve_sucess_message = "Hospital inform retrieve returend success"
    create_success_message = "Hospital is the create"
    status_code = 600
    response = {
        "status": None,
        "msg": None,
        "data": None
    }

    @action(detail=False, methods=['POST'])
    def hospital_(self, request):
        self.response.update({
            "status": True,
            "msg": 'hospital inform is the right',
            "data":{}
        })
        return Response(self.response)

class HospitalBranchModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    model = HospitalBranch
    queryset= HospitalBranch.objects.all()
    serializer_class = HospitalBranchSerializers
    list_success_message ="Hospital branch list returend success"
    retrieve_sucess_message = "Hospital branch retrieve returend success"
    create_success_message = "Hospital branchis the create"
    status_code = 200
    response = {
        "status": None,
        "msg": None,
        "data": None
    }

    @action(detail=False, methods=['POST'])
    def hospital_branch(self, request):
        self.response.update({
            "status": True,
            "msg": "the hospital of yes",
            "data": {}
        })
        return Response(self.response)


@api_view(['DELETE'])
def h_branch(request):
    id = request.data.get('id')
    if id is None or id == "":
        return Response(" please branch id")
    HospitalBranch.objects.filter(
        id=id).delete()
    response = {
        "status": True,
        "msg": "The hospital id is delete",
        "data":{}
    }
    return Response(response)

