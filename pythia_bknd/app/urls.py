from django.urls import path
from . import views

urlpatterns = [
    path("get_students/", views.get_students,name='get_students_app'),
    path("add_student/", views.add_student,name='add_student_app'),
    path("modify_student/", views.modify_student,name='modify_student_app'),
    path("delete_student/", views.delete_student,name='delete_student_app')
]

