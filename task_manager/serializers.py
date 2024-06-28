from rest_framework import serializers
from .models import Employee, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer("tasks", many=True)
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'job_title', 'tasks', 'is_active')