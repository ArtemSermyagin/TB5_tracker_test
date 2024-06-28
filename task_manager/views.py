from django.db.models import Count
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from .models import Employee, Task
from .serializers import EmployeeSerializer, TaskSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class BusyEmployeesListAPIView(ListAPIView):
    queryset = Employee.objects.annotate(count_tasks=Count('tasks')).all().order_by('-count_tasks')
    # employees_with_count_tasks = queryset.all()
    serializer_class = EmployeeSerializer

    # def get_queryset(self):
    #     queryset = Employee.objects.filter(tasks__is_active=True) \
    #         .annotate(count_tasks=Count('tasks')) \
    #         .order_by('-count_tasks')
    #
    #     return queryset

