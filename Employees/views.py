# from django.shortcuts import render
from  .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics,mixins
from django.http import Http404

# Create your views here.

#class based views

# class employees(APIView):
#     def get(self,request):
#         employees=Employee.objects.all()
#         serializers=EmployeeSerializer(employees,many=True)
#         return Response(serializers.data,status=status.HTTP_200_OK)

#     def post(self,request):
#         serializers=EmployeeSerializer(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_201_CREATED)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)


# class EmmployeeDetails(APIView):
#     def get_object(self,pk):
#         try:
#            return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404
        
#     def get(self,request,pk):
#         employee=self.get_object(pk)
#         serializers=EmployeeSerializer(employee)
#         return Response(serializers.data,status=status.HTTP_200_OK)
    
        
#     def put(self,request,pk):
#         employee=self.get_object(pk)
#         serializers=EmployeeSerializer(employee,data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data,status=status.HTTP_200_OK)
#         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,pk):
#         employee=self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    


# Mixin View
# class employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer

#     def get(self,request):
#         return self.list(request)
    
#     def post(self,request):
#         return self.create(request)
    

# class EmmployeeDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer

#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#     def put(self, request,pk):
#         return self.update(request,pk)
    
#     def delete(self,request,pk):
#         return self.destroy(request,pk)



#Generic views
#sepate the list and create view
# class employees(generics.ListAPIView,generics.CreateAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer

#together the list and create view
class employees(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

#separate the retrieve,update and delete view
# class EmmployeeDetails(generics.RetrieveAPIView,generics.UpdateAPIView, generics.DestroyAPIView):
#     queryset=Employee.objects.all()
#     serializer_class=EmployeeSerializer
#     lookup_field='pk'

#together the retrieve,update and delete view
class EmmployeeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    lookup_field='pk'