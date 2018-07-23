
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serialisers import team_dataSerialiser
from .models import user_record, team_data
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt


# Create your views here.


#vashisht's views
def example(request):
    var=team.objects.all()

#neeraj's views
def user_register(request):
    try:
        data = json.loads(request.body)
        namee = data['name']
        tagg = data['tag']
        rec = user_record(name = namee, tag = tagg)
        rec.save()
    except:
        print('no data')



def checkusername(request):
    data = json.loads(request.body)
    userr = data['name']
    if user_record.objects.filter(name = userr).exists():
        return False
    else:
        return True


@csrf_exempt
class teams(APIView):
    def get(self, request):
        teams = team_data.objects.all()
        serializer = team_dataSerialiser(teams, many = True)
        return Response(serializer.data)


    def post(self,request):
        serializer = team_dataSerialiser(data=request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



