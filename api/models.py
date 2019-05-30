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

WEEKDAYS = [
    (2, 'SEGUNDA'),
    (3, 'TERCA'),
    (4, 'QUARTA'),
    (5, 'QUINTA'),
    (6, 'SEXTA'),
]

TIMES = [
    ('NA', 'NONE'),
    ('M', 'MORNING'),
    ('A', 'AFTERNOON'),
    ('N', 'NIGHT'),
]

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    institution = models.CharField(max_length=200, choices=ALL_INSTITUTIONS)

class Day(models.Model):
    weekday_id = models.IntegerField(choices=WEEKDAYS, unique=True, null=False)
    departure = models.CharField(max_length=50, choices=TIMES)
    arrival = models.CharField(max_length=50, choices=TIMES)
    student = models.ForeignKey(Student, related_name='schedule', on_delete=models.CASCADE, blank=True)

REQUEST = {
    "name": "teste",
    "email": "teste@ererr.com",
    "institution": "UFRN",
    "schedule": [
        {
            "weekday_id": 2,
            "departure": "NA",
            "arrival": "NA"
        },
        {
            "weekday_id": 3,
            "departure": "NA",
            "arrival": "NA"
        },
        {
            "weekday_id": 4,
            "departure": "NA",
            "arrival": "NA"
        },
        {
            "weekday_id": 5,
            "departure": "NA",
            "arrival": "NA"
        },
        {
            "weekday_id": 6,
            "departure": "NA",
            "arrival": "NA"
        }
    ]
}