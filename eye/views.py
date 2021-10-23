from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Events
from .serializers import EventsSerializer
from rest_framework import status
# Create your views here.

class EventView(APIView):
    def post(self,request,*args,**kwargs):
        if 'element' in request.data['data']:
            element = request.data['data']['element']
        else:
            element = None
        if 'form' in request.data['data']:
            firstName = request.data['data']['form']['first_name']
            lastName = request.data['data']['form']['last_name']
        else:
            firstName = None
            lastName = None

        data_dict = {
            'session_id':request.data['session_id'],
            'category':request.data['category'],
            'name':request.data['name'],
            'host':request.data['data']['host'],
            'path':request.data['data']['path'],
            'first_name':firstName,
            'last_name':lastName,
            'element':element,
            'timestamp':request.data['timestamp'],
        }
        serializer = EventsSerializer(data=data_dict)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)