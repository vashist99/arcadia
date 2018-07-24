
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serialisers import team_dataSerialiser, user_recordSerialiser
from .models import user_record, team_data, team
import json
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def example(request):
    var=team.objects.all()


class user_register(APIView):
    def post(self, request):
        serializer = user_recordSerialiser(data=(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)

def checkusername(request):
    data = json.loads(request.body)
    userr = data['name']
    if user_record.objects.filter(name = userr).exists():
        return False
    else:
        return True




class teams(APIView):
    def get(self, request):
        teams = team_data.objects.all()
        serializer = team_dataSerialiser(teams, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = team_dataSerialiser(data=(request.data))
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(request.data, status=status.HTTP_400_BAD_REQUEST)






