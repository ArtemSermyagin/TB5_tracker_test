import django_filters

from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Announcement
        fields = ['title']