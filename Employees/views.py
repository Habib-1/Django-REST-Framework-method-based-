# from django.shortcuts import render
from  .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.
class employees(APIView):
    def get(self,request):
        employees=Employee.objects.all()
        serializers=EmployeeSerializer(employees,many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializers=EmployeeSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


class EmmployeeDetails(APIView):
    def get_object(self,pk):
        try:
           return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        employee=self.get_object(pk)
        serializers=EmployeeSerializer(employee)
        return Response(serializers.data,status=status.HTTP_200_OK)
    
        
    def put(self,request,pk):
        employee=self.get_object(pk)
        serializers=EmployeeSerializer(employee,data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_200_OK)
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        employee=self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)