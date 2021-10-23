from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class EventView(APIView):
    def post(self,request,*args,**kwargs):
        print('x')
        return Response(data={'it worked'})