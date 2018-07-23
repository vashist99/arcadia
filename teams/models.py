from django.db import models

from django.contrib.auth.models import User


status_choices = [

    ('w', 'winner'),
    ('p', 'participating'),
    ('d', 'disqualified')

]
# Create your models here.

class user_record(models.Model):
    username = models.ForeignKey(User, related_name='user_name', on_delete=models.CASCADE)
    team = models.CharField(max_length=300)
    #team_status = models.CharField(max_length=300, choices = status_choices)
