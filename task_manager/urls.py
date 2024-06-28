from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, TaskViewSet, BusyEmployeesListAPIView

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'tasks', TaskViewSet)


urlpatterns = router.urls
urlpatterns += [
    path('busy_employees/', BusyEmployeesListAPIView.as_view(), name='busy_employees')
]