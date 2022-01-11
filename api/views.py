from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

from api.serializers import StudentDataSerializer, StudentResultSerializer
from api.models import StudentData, StudentResult

@api_view(['GET', 'POST'])
def student_data_list(request):
    if request.method == 'GET':
        student_data = StudentData.objects.all()
        serializer = StudentDataSerializer(student_data, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PATCH', 'DELETE'])
def student_data_detail(request, pk):
    try:
        student_data = StudentData.objects.get(pk=pk)
    except StudentData.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = StudentDataSerializer(student_data)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = StudentDataSerializer(student_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        student_data.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
def student_result_list(request):
    if request.method == 'GET':
        student_result = StudentResult.objects.all()
        serializer = StudentResultSerializer(student_result, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = StudentResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PATCH', 'DELETE'])
def student_result_detail(request, pk):
    try:
        student_result = StudentResult.objects.get(pk=pk)
    except StudentResult.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = StudentResultSerializer(student_result)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = StudentResultSerializer(student_result, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        student_result.delete()
        return Response(status=204)

@api_view(['GET', 'POST'])
def student_data_result_list(request):
    if request.method == 'GET':
        student_data = StudentData.objects.all()
        student_result = StudentResult.objects.all()
        serializer = StudentDataSerializer(student_data, many=True)
        serializer2 = StudentResultSerializer(student_result, many=True)
        return Response({'student_data': serializer.data, 'student_result': serializer2.data})
    elif request.method == 'POST':
        serializer = StudentDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PATCH', 'DELETE'])
def student_data_result_detail(request, pk):
    try:
        student_data = StudentData.objects.get(pk=pk)
    except StudentData.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = StudentDataSerializer(student_data)
        return Response(serializer.data)
    elif request.method == 'PATCH':
        serializer = StudentDataSerializer(student_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        student_data.delete()
        return Response(status=204)