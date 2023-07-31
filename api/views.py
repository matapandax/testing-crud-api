from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status

from api.models import Student
from .serializer import StudentSerializer

@api_view(['GET'])
def index(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def studentView(request, pk):
    try:
        student = Student.objects.get(id=pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def studentAdd(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def studentUpdate(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = StudentSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status': status.HTTP_200_OK,
            'student': serializer.data,
            'message': 'Updated successfully'
        })
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def studentDelete(request, pk):
    try:
        student = Student.objects.get(id=pk)
        student.delete()

        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)

        return Response({
            'status': status.HTTP_200_OK,
            'students': serializer.data,
            'message': 'Student Deleted successfully'
        })
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
