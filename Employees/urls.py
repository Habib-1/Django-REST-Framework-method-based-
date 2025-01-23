from django.urls import path
from . import views
urlpatterns = [
   
    path('employees/', views.employees.as_view()),
    path('employees/<int:pk>/', views.EmmployeeDetails.as_view()),
]