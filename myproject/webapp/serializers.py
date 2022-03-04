from rest_framework import serializers
from rest_framework import employees

class employeeSerializer(serializers.ModelSerializer): #serializer is convert to json format

    class Meta:
        model= employees
        # fields= ('firstname','lastname')
        fields='__all__' #it'll print all the fields