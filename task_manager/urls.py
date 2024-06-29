from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, TaskViewSet, BusyEmployeesListAPIView, TaskFreeListAPIView, EmployeeSearchDetailAPIView, TaskListAPIView

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'tasks', TaskViewSet)


urlpatterns = router.urls
urlpatterns += [
    path('busy_employees/', BusyEmployeesListAPIView.as_view(), name='busy_employees'),
    path('tasks/free/', TaskFreeListAPIView.as_view(), name='task_free'),
    path('tasks/<int:pk>/employer_search/', EmployeeSearchDetailAPIView.as_view(), name='employer_search'),
    path('tasks/', TaskListAPIView.as_view(), name='tasks')
]