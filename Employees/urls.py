from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('employee',views.EmployeeViewSets,basename='employee')
urlpatterns = [
    #Working on Class Based view,Generic view,mixins view
    # path('employees/', views.employees.as_view()),
    # path('employees/<int:pk>/', views.EmmployeeDetails.as_view()),

    #working on router and viewsets
    path('',include(router.urls)),
]