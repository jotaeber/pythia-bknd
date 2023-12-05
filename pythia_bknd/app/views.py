from django.shortcuts import render
from django.http import HttpResponse

from app.models import Student

from app import serializers

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_students(request):
    '''
    Listado de estudiantes
    '''
    students = Student.objects.all()
    serializers = serializers.StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_student(request):
    serializer = serializer.StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {'status': 'OK!',
                    'message': 'Estudiante ingresado correctamente',
                    'data': serializer.data}
        return Response(data=response, status=status.HTTP_201_CREATED)
    
    response = {'status': 'ERROR...',
                'message': 'Hubo un error al ingresar el estudiante...',
                'errors': serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def student_check(request, id):
    '''
    Ver un estudiante:
    '''
    try:
        #Se busca la pelicula en base por el id
        movie = Student.objects.get(pk=id)        
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Estudiante no encontrado')

    serializer = serializers.StudentSerializer(Student)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_student(request, id):
    '''
    Eliminar un estudiante:
    '''
    try:
        student = Student.objects.get(pk=id)        
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data='Estudiante no encontrado...')
    student.delete()
    return Response({'message':'Se elimino estudiante'},status=status.HTTP_200_OK)


@api_view(['PUT'])
def modify_student(request, id):
    '''
    Modificar un estudiante:.
    '''
    try:
        student = Student.objects.get(pk=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,data='Estudiante no encontrado')
    
    serializer = serializers.MovieSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        response = {'status':'OK',
                    'message':'Estudiante modificado exitosamente!',
                    'data':serializer.data}
        return Response(data=response)
    
    response = {'status':'Error',
                'message':'No se ha podido modificar el estudiante',
                'errors':serializer.errors}
    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)