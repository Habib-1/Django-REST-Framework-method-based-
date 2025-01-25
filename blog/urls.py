from django.urls import path
from . import views
urlpatterns = [
    path('blog/',views.BlogView.as_view()),
    path('comment/',views.CommentView.as_view()),
    path('blog/<int:pk>/',views.BlogDetails.as_view()),
    path('comment/<int:pk>/',views.CommentDetails.as_view()),
]

