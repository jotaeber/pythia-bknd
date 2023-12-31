from rest_framework import serializers
from app.models import Student

class StudentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Student
    fields = ['id','name','surname','birth_date','course','ssn','email']