from django.db.models import Count, Q
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Employee, Task
from .serializers import EmployeeSerializer, TaskSerializer, EmployerShowSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class BusyEmployeesListAPIView(ListAPIView):
    queryset = Employee.objects.annotate(
        count_tasks=Count("tasks", filter=Q(tasks__is_active=True))
    ).all().order_by('-count_tasks')
    serializer_class = EmployeeSerializer


class TaskFreeListAPIView(ListAPIView):
    queryset = Task.objects.filter(employer__isnull=True, parent__employer__isnull=False)
    serializer_class = TaskSerializer


class EmployeeSearchDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, id=kwargs['pk'])
        allowed_tasks = Task.objects.filter(employer__isnull=True, parent__employer__isnull=False)
        if task not in allowed_tasks:
            raise ValidationError({"error": "This task has a parent or employer."})
        least_busy_employer = Employee.objects.annotate(
            count_tasks=Count("tasks", filter=Q(tasks__is_active=True))
        ).all().order_by('count_tasks').first()
        task_parent_employer = task.parent.employer
        count_task_parent_employer = task_parent_employer.tasks.all().count()
        different_count_tasks = count_task_parent_employer - least_busy_employer.count_tasks
        if different_count_tasks <= 2:
            return Response(EmployeeSerializer(task_parent_employer).data)
        else:
            return Response(EmployeeSerializer(least_busy_employer).data)

class TaskListAPIView(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

