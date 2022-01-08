from api.models import StudentData, StudentResult

from rest_framework import serializers


class StudentDataSerializer(serializers.ModelSerializer):


    class Meta:
        model = StudentData
        fields = '__all__'
        read_only = ['id']

class StudentResultSerializer(serializers.ModelSerializer):

    student = StudentDataSerializer(many=False, read_only=True)

    class Meta:
        model = StudentResult
        fields = '__all__'
        read_only = ['id']
