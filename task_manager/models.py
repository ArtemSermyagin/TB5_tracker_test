from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, default='default_value')
    middle_name = models.CharField(max_length=100, default='default_value')
    job_title = models.CharField(max_length=50)


class Task(models.Model):
    name = models.CharField(max_length=100)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    employer_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    completion_date = models.DateField()
    is_active = models.CharField(max_length=20)
