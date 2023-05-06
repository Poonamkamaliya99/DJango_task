from django.urls import path

from .views import Employees, EmployeeSearch
from app import views

urlpatterns = [
    path('employee/', Employees.as_view(), name='employee'),
    path('employee/<id>', Employees.as_view(), name='employee'),
    path('search/', EmployeeSearch.as_view(), name='search'),
]