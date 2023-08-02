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
    # Add the following URL patterns for Course views
    path('course/', views.course_list, name="course-list"),
    path('course/<int:pk>/', views.course_detail, name="course-detail"),
    path('course-create/', views.course_create, name="course-create"),
    path('course-update/<int:pk>/', views.course_update, name="course-update"),
    path('course-delete/<int:pk>/', views.course_delete, name="course-delete"),
  
]
