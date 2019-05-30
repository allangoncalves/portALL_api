from rest_framework import generics
from .models import Student, Day
from .serializers import StudentSerializer, DaySerializer

# Create your views here.

class ListStudent(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ListDay(generics.ListCreateAPIView):
    queryset = Day.objects.all()
    serializer_class = DaySerializer