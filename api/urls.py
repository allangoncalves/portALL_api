from django.urls import path

from .views import ListStudent, ListDay

urlpatterns = [
    path('student/', ListStudent.as_view()),
    path('day/', ListDay.as_view())
]