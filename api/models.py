from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name
    
class OpenedxCourse(models.Model):
    course_code = models.CharField(max_length=100)
    course_name = models.CharField(max_length=255)