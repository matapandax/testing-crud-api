from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="/"),
    path('student-view/<str:pk>/', views.studentView, name="studentview"),
    path('add-student/', views.studentAdd, name="studentadd"),
]