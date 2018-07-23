from django.shortcuts import render
from django.http import HttpResponse
from .models import team

def example(request):
    var=team.objects.all()
    def rec(*args):
        

    #return HttpResponse(var[2])


# Create your views here.
