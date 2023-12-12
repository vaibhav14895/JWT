from attr import fields
from rest_framework import serializers
from .models import student


class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model=student
        fields= ['id','name','roll','city']