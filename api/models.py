from django.db import models

# Create your models here.
ALL_INSTITUTIONS = [
    ('UFRN', 'Universidade Federal do Rio Grande do Norte'),
    ('IFRN', 'IFRN'),
    ('UNP', 'UNIFACEX'),
    ('NASSAU', 'NASSAU'),
    ('ESTACIO', 'ESTACIO'),
    ('CT-GAS', 'CT-GAS'),
    ('OUTRO', 'Outro'),
]

TIMES = [
    ('NA', 'NONE'),
    ('M', 'MORNING'),
    ('A', 'AFTERNOON'),
    ('N', 'NIGHT'),
]

class Day(models.Model):
    departure = models.CharField(max_length=50, choices=TIMES)
    arrival = models.CharField(max_length=50, choices=TIMES)

class Schedule(models.Model):
    monday = models.OneToOneField(Day, on_delete=models.CASCADE, related_name='monday')
    tuesday = models.OneToOneField(Day, on_delete=models.CASCADE, related_name='tuesday')
    wednesday = models.OneToOneField(Day, on_delete=models.CASCADE, related_name='wednesday')
    thursday = models.OneToOneField(Day, on_delete=models.CASCADE, related_name='thursday')
    friday = models.OneToOneField(Day, on_delete=models.CASCADE, related_name='friday')

class Student(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField()
    institution = models.CharField(max_length=200, choices=ALL_INSTITUTIONS)
    schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE, null=True, blank=True)
