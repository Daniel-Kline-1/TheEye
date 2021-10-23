from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Events
from .serializers import EventsSerializer
from rest_framework import status
import datetime
# Create your views here.

class EventView(APIView):
    def post(self,request,*args,**kwargs):
        # changes timestamp from string to timstamp form to compair time
        timestamp = datetime.datetime.fromisoformat(request.data['timestamp'])

        if timestamp > datetime.datetime.now():
            return Response(data={'timestamp is invalid, must be present or past'},status=status.HTTP_400_BAD_REQUEST)

        # if element is not included, then make it null
        if 'element' in request.data['data']:
            element = request.data['data']['element']
        else:
            element = None

        # if form is not included then make first and last name null
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
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SessionView(APIView):
    def get(self,request,*args,**kwargs):
        session = request.GET.get('session','')

        # session id is needed to make query
        if session == '':
            return Response(data={'Missing session_id'}, 
            status=status.HTTP_404_NOT_FOUND)



        qs = Events.object.filter(session_id = session)
        serializer = EventsSerializer(qs, many=True)
        return Response(serializer.data)



class CategoryView(APIView):
    def get(self,request,*args,**kwargs):
        category = request.GET.get('category','')
        # category is needed to make query
        if category == '':
            return Response(data={'Missing category'}, 
            status=status.HTTP_404_NOT_FOUND)


        qs = Events.object.filter(category = category)
        serializer = EventsSerializer(qs, many=True)
        return Response(serializer.data)


class TimeView(APIView):
    def get(self,request,*args,**kwargs):
        time_i = request.GET.get('timeStart','')
        time_f = request.GET.get('timeEnd','')
        # initial and final times are needed to make query
        if time_i == '':
            return Response(data={'Missing start time'}, 
            status=status.HTTP_404_NOT_FOUND)
        
        if time_f == '':
            return Response(data={'Missing end time'}, 
            status=status.HTTP_404_NOT_FOUND)
        

        # see if given times can be converted to datetimes, if not then 
        # they were entered incorectly
        try:
            time_start = datetime.datetime.fromisoformat(time_i)
        except:
            return Response(data={'invalid start time'}, status=status.HTTP_400_BAD_REQUEST)

        try:

            time_end = datetime.datetime.fromisoformat(time_f)
        except:
            return Response(data={'invalid end time'}, status=status.HTTP_400_BAD_REQUEST)


        qs = Events.objects.filter(timestamp__range = [time_start,time_end])
        
        
        serializer = EventsSerializer(qs, many=True)
        return Response(serializer.data)