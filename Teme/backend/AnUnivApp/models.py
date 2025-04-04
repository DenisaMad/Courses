from django.db import models
from rest_framework import serializers

# Create your models here.

class AnUniversitar(models.Model):
    an_start = models.IntegerField(null=False, blank=False)
    an_end = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return str(self.an_start)+"-"+str(self.an_end)
    
    
class Create_AnUniv_request(serializers.Serializer):
    an_start=serializers.CharField()
    an_end=serializers.CharField()
    
class AnUniv_serializer(serializers.ModelSerializer):
    class Meta:
        model=AnUniversitar
        fields="__all__"
