from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.response import Response
from .serializers import InfoSerializer
from rest_framework import permissions

# Create your views here.

class TestAPIView(APIView):
    def get(self, request):
        return Response('ok')

    def post(self, request):
        da = InfoSerializer(data=request.data)
        if not da.is_valid():
            return Response('bad request', status=status.HTTP_400_BAD_REQUEST)

        print('====> data = ', da.data)
        return Response('ok nhan data thanh cong', status=status.HTTP_200_OK)
        
class NotAuthenAPIView(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request): 
        return Response('check not authen')