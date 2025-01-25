from django.shortcuts import render
from rest_framework import generics
from .models import Blog,Comments
from .serializers import BlogSerializer, CommentSerializer
# Create your views here.
class BlogView(generics.ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer

class CommentView(generics.ListCreateAPIView):
    queryset=Comments.objects.all()
    serializer_class=CommentSerializer

class BlogDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    lookup_field='pk'

class CommentDetails(generics.RetrieveDestroyAPIView):
    queryset=Comments.objects.all()
    serializer_class=CommentSerializer
    lookup_field='pk'
