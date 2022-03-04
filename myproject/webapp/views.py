from django.shortcuts import render #it's default

# in this file we need to request API and get the JSON back
# Create your views here.

from django.http import HttpResponse #for return the response
from django.shortcuts import get_object_or_404  #when some information is does not exist in database that time it will return 404
from rest_framework.views import APIView #it is use for view of normal data
from rest_framework.response import Response #get back to the response or status(if everything fine then it'll return 200)
from rest_framework import status #sent back the status
from . models import employees #model name is employees
from . serializers import employeeSerializer #model name is serializer

class employeeList(APIView):
    #get method- use for return all the employees in a model
    #post method- use for create a new employee
    def get(self,request):
        employees1 = employees.objects.all()
        serializer=employeeSerializer(employees1, many=True)
        return Response(serializer.data)


    def post(self):
        pass
