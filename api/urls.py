from django.urls import path

from .views import ListStudent

urlpatterns = [
    path('student/', ListStudent.as_view()),
]