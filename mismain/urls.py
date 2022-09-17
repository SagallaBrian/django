from django.urls import path
from . import views

urlpatterns = [
    path('', views.employeeList, name='listEmployees'),
    path('addemp', views.addEmployee, name='addemployee'),
    path('editemp/<str:empid>/', views.editEmployee, name='editemployee'),
    path('delemp/<str:empid>/',  views.delEmployee, name='deletemployee'),


    path('deplist/', views.departmentList, name='listdepartment'),
    path('depadd', views.addDepartment, name='addepartment'),
    path('depedit/<str:depid>/',  views.editDepartment, name='editdepartment'),
    path('depdel/<str:depid>/',  views.delDepartment, name='deldepartment'),
]
