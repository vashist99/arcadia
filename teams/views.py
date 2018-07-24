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
from .forms import user




# Create your views here.
def view_teams(request):
    with open("Frontend/teams.json","r") as read_file:
        json_data=json.load(read_file)
    return  HttpResponse(json_data, content_type='application/json')
    #response['Content-Disposition'] = 'attachment; filename="teams.json"'

def user_reg(request):
    if request.method=='POST':
        obj=user(request.POST)
        with open("users.json","w") as write_file:
            json.dump(obj)
    else:
        obj=user()
        return render(request,'arcadia/index.html',{'forms':obj})


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
