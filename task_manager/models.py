from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)


class Task(models.Model):
    name = models.CharField(max_length=100)
    parent_task = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    executor = models.ForeignKey(Employee, on_delete=models.CASCADE)
    deadline = models.DateField()
    status = models.CharField(max_length=20)
