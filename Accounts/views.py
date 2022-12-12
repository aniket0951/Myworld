from django.shortcuts import render
from .models import PatientPayment,OnlineRegister,PatientLogin
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from .serializers import PatientPaymentSerializers,OnlineRegisterSerializers,PatientLoginSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from utils import custom_viewsets
from rest_framework.permissions import IsAdminUser, AllowAny


class PatientPaymentModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    model = PatientPayment
    queryset = PatientPayment.objects.all()
    serializer_class = PatientPaymentSerializers
    list_success_message = "Patient payment list returend success"
    retrieve_sucess_message = "Patient payment retrieve returend success" 
    status_code = 200
    response = {
        "status" : None,
        "msg" : None,
        "data" : None
    }

    @action(detail=False, methods=["PUT"])
    def testAPI(self, request):
        self.response.update({
            "status":200,
            "msg": "API get heated !",
            "data": None
        })

        return Response(self.response)        

@api_view(['DELETE'])
def patient_register(request):
    id = request.data.get('id')
    if id is None or id == "":
        return Response('please id')
    OnlineRegister.objects.filter(
        id=id).delete()
    response = {
        "satus": True,
        "mag": 'patient register id delete success',
        "error": 'null',
        "data" : {}
    }
    return Response(response)


class OnlineRegisterModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    model = OnlineRegister
    queryset =  OnlineRegister.objects.all()
    serializer_class = OnlineRegisterSerializers
    list_success_message = "Patient register list returend success"
    retrieve_sucess_message = "Patient register retrieve returend success"
    status_code = 200 
    response = {
        "status": None,
        "mag" :None,
        "data": None
    }
    
    @action(detail=False, methods=["POST"])
    def onlineRegister(self, request):
        self.response.update({
            "status": 200,
            "mag": 'the patient register success',
            "data": {}
        })
        return Response(self.response)

class PatientLoginModelViewSet(custom_viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    model = PatientLogin
    queryset = PatientLogin.objects.all()
    serializer_class = PatientLoginSerializers
    list_success_message ="Patient login list returend success"
    retrieve_sucess_message = "Patient login retrieve returend success"
    status_code = 200
    response = {
        "status": None,
        "msg": None,
        "data":None
    }
    @action(detail=False, methods=['POST'])
    def patient_login(self, request):
        self.response.update({
            "status": 200,
            "msg": 'The patient login success',
            "data": {}
        })
        return Response(self.response)

@api_view(['DELETE'])
def p_login(request):
    id = request.data.get('id')
    if id is None or id == "":
        return Response('please id')
    PatientLogin.objects.filter(
        id=id).delete()
    response = {
        "status": True,
        "msg": 'patint id delete success',
        "error": 'null',
        "data": {}
    }
    return Response(response)
