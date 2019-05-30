from rest_framework import serializers
from .models import Student, Day



class DaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('departure', 'arrival', 'weekday_id')

class StudentSerializer(serializers.ModelSerializer):
    schedule = DaySerializer(many=True, required=False)

    class Meta:
        model = Student
        fields = ('id', 'name', 'email', 'institution', 'schedule')

    def create(self, validated_data):
        schedule_data = validated_data.pop('schedule')
        student = Student.objects.create(**validated_data)
        for day in schedule_data:
            Day.objects.create(student=student, **day)
        return student
    
    def validate_items(self, items):
        if len(items) > 5:
            raise serializers.ValidationError("Too many weekdays")





