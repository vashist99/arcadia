from django.shortcuts import render
from django.http import HttpResponse
from .models import team


def example(request):
    var=team.objects.all()


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


    #return HttpResponse(var[2])


# Create your views here.
