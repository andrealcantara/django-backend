from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.
from apps.Employees.models import Departments
from apps.Employees.serializers import DepartmentSerializer


@csrf_exempt
class DepartmentsAPI(RetrieveUpdateDestroyAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentSerializer
    lookup_url_kwarg = 'departments_id'



    # def get(self, request, format=None):
    #     departments = Departments.objects.all();
    #     departments_serializable = DepartmentSerializer(departments, many=True)
    #     return JsonResponse(departments_serializable.data, safe=False)
    #
    # def post(self, request, format=None):
    #     department_data = JSONParser().parse(request)
    #     department_serializable = DepartmentSerializer(data=department_data)
    #     if department_serializable.is_valid():
    #         department_serializable.save()
    #         return JsonResponse("Adicionado com Sucesso.", safe=False)
    #     return JsonResponse("Failed to add", safe=False)
    #
    # def put(self, request, format=None):
    #     department_data = JSONParser().parse(request)
    #     department = Departments.objects.get(id=department_data['id'])
    #     department_serializable = DepartmentSerializer(department, data=department_data)
    #     if department_serializable.is_valid():
    #         department_serializable.save()
    #         return JsonResponse("Atualizado com sucesso", safe=False)
    #     return JsonResponse("Falha ao Atualizar", safe=False)
    #
    # def delete(self, request, format=None):
    #     id = request.DELETE['id']
    #     department = Departments.objects.get(id)
    #     department.delete()
    #     return JsonResponse("Deletado com Sucesso")
