from django.urls import re_path
from apps.Employees import views

urlpatterns = [
    re_path('(?P<id>[0-9]{4})/$', views.departmentAPI),
]

