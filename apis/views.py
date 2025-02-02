# from django.shortcuts import render
# from django.http import JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# Create your views here.


@api_view(['GET','POST'])
def students(request):
  if request.method=="GET":
    students=Student.objects.all()
    serializer=StudentSerializer(students,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK) 
  
  elif request.method=="POST":
    serializer=StudentSerializer(data=request.data)

    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['GET','PUT','DELETE'])
def student(request,pk):
  try:
    student=Student.objects.get(pk=pk)
  except Student.DoesNotExist:
   return Response({"error":"Student not found"},status=status.HTTP_404_NOT_FOUND)
  
  if request.method=="GET":
    serializer=StudentSerializer(student)
    return Response(serializer.data,status=status.HTTP_200_OK)  
  
  if request.method=="PUT":
    serializer=StudentSerializer(student,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  if request.method=="DELETE":
    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)