
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Departments, Employee
from .serializers import DepartmentSerializer, EmployeeSerializer
# Create your views here.


@csrf_exempt
def departmentAPI(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all();
        departments_serializable = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializable.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializable = DepartmentSerializer(data=department_data)
        if department_serializable.is_valid():
            department_serializable.save()
            return JsonResponse("Adicionado com Sucesso.", safe=False)
        return JsonResponse("Failed to add", safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(id=department_data['id'])
        department_serializable = DepartmentSerializer(department, data=department_data)
        if department_serializable.is_valid():
            department_serializable.save()
            return JsonResponse("Atualizado com sucesso", safe=False)
        return JsonResponse("Falha ao Atualizar", safe=False)
    elif request.method == 'DELETE':
        department = Departments.objects.get(id)
        department.delete()
        return JsonResponse("Deletado com Sucesso")

