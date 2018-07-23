
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
def team_register(request):
    datt = json.loads(request.body)
    s = team_dataSerialiser(data = request.data)
    dataa = datt['teams']
    for data in dataa:
        a = data['name']
        b = data['leader']
        c = data['members']
        c0 = c[0]['name']
        d0 = c[0]['tag']
        c1 = c[1]['name']
        d1 = c[1]['tag']
        c2 = c[2]['name']
        d2 = c[2]['tag']
        c3 = c[3]['name']
        d3 = c[3]['tag']
        c4 = c[4]['name']
        d4 = c[4]['tag']
        rec = team_data(
                team_name = a, leader = b,
                member = c0, membertag = d0,
                member5=c1, member5tag = d1,
                member2=c2, member2tag=d2,
                member3=c3, member3tag=d4,
                member4=c4, member4tag=d3,


                     )
        rec.save()
        return Response(s.data, status=status.HTTP_201_CREATED)


class teams(APIView):
    def get(self, request):
        teams = team_data.objects.all()
        serializer = team_dataSerialiser(teams, many = True)
        return Response(serializer.data)




