from django.contrib import admin

from task_manager.models import Employee, Task


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'job_title'
    )
    search_fields = ('job_title',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'employer',
        'completion_date',
        'is_active'
    )
    search_fields = ('is_active',)