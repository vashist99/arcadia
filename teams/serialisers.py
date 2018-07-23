from rest_framework import serializers

from .models import team_data

class team_dataSerialiser(serializers.ModelSerializer):
    class Meta:
        model  = team_data
        fields = '__all__'
