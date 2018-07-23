
from django.shortcuts import render
from .models import user_record, User
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate



# Create your views here.


def register(request):
    try:
        data = json.loads(request.body)
        #print(data)
        name = data['username']
        passw = data['password']
        team = data['team']
        user = authenticate(username = name, password = passw)
        rec = user_record(username = name, team = team)
        rec.save()


    except:
        print('no data')



def checkusername(request):
    data = json.loads(request.body)
    userr = data['username']
    if User.objects.filter(username=userr).exists():
        return False
    else:
        return True

#def teamview(request):
 #   x = user_record.objects.order_by().values('team').distinct()
  #  return JsonResponse(x)



