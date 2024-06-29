from rest_framework import serializers
from .models import Employee, Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField()
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'middle_name', 'job_title', 'tasks')

    def get_tasks(self, obj):
        return TaskSerializer(obj.tasks.filter(is_active=True), many=True).data