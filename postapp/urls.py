from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('employeedetails/<int:id>', views.employeedetails, name='employeedetails'),
    path('employeedetails', views.employee, name='employee'),
]
