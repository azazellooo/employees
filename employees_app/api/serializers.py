from rest_framework import serializers

from .models import ProgrammingLanguage, Department, Employee


class ProgrammingLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguage
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer()
    programming_language = ProgrammingLanguageSerializer()
    class Meta:
        model = Employee
        fields = '__all__'
