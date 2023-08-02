from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status

from api.models import Student
from api.models import OpenedxCourse
from .serializer import OpenedxSerializer
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


@api_view(['GET'])
def course_list(request):
    courses = OpenedxCourse.objects.all()
    serializer = OpenedxSerializer(courses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def course_detail(request, pk):
    try:
        course = OpenedxCourse.objects.get(pk=pk)
        serializer = OpenedxSerializer(course)
        return Response(serializer.data)
    except OpenedxCourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def course_create(request):
    serializer = OpenedxSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def course_update(request, pk):
    try:
        course = OpenedxCourse.objects.get(pk=pk)
    except OpenedxCourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = OpenedxSerializer(instance=course, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def course_delete(request, pk):
    try:
        course = OpenedxCourse.objects.get(pk=pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except OpenedxCourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)