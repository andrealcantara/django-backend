from django.urls import re_path, path, include
from rest_framework import routers
from apps.Employees.views import DepartmentsAPI

# router = routers.DefaultRouter()
# router.register(r'^departments/', DepartmentsAPI, 'department-all')

urlpatterns = [
    path('departments', DepartmentsAPI, name='dp-all'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


