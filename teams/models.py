from django.db import models

# Create your models here.
class team(models.Model):
    team_name=models.CharField(max_length=100)

    def __str__(self):
        return self.team_name
