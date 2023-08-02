from rest_framework import serializers

from .models import Student
from .models import OpenedxCourse


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

class OpenedxSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpenedxCourse
        fields= '__all__'