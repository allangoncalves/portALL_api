from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

# Create your views here.

class ListStudent(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer