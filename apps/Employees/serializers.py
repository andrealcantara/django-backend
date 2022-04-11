from rest_framework import serializers
from .models import Departments, Employee


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('id', 'name')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'name', 'department', 'dateOfJoin', 'photoFileName')

