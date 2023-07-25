from rest_framework.response import Response 
from rest_framework.decorators import api_view

from api.models import Student
from .serializer import StudentSerializer
# Create your views here.



@api_view(['GET'])
def index(request):
    student = Student.objects.all()
    serialstudents = StudentSerializer(student, many=True)
    return Response(serialstudents.data)
