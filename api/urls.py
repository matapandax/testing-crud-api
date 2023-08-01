from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('student-view/<str:pk>/', views.studentView, name="studentview"),
    path('add-student/', views.studentAdd, name="studentadd"),
    path('update-student/<str:pk>/', views.studentUpdate, name="studentupdate"),
    path('delete-student/<str:pk>/', views.studentDelete, name="studentdelete"),
    path('react/', TemplateView.as_view(template_name='frontend/build/index.html'), name="react"),
]
