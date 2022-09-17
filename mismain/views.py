from django.shortcuts import redirect, render
from django.contrib import messages
from . models import Department, Employee
from . forms import DepartmentForm, EmployeeForm


# Create your views here.


def departmentList(request):
    if not request.user.is_authenticated:
        return redirect('login')

    department = Department.objects.all()
    return render(request, 'depart.html', {'name': 'Department List', 'departmentlist': department})


def addDepartment(request):
    if not request.user.is_authenticated:
        return redirect('login')

    form = DepartmentForm()
    if request.method == 'POST':

        postform = DepartmentForm(request.POST)
        if postform.is_valid():
            postform.save()
            return redirect('listdepartment')
        else:
            messages.error(request, 'Document deleted.')

    return render(request, 'depart_add_edit.html', {'dpform': form, 'name': 'Add Department', })


def editDepartment(request, depid):
    if not request.user.is_authenticated:
        return redirect('login')

    department = Department.objects.get(id=depid)
    form = DepartmentForm(instance=department)

    if request.method == 'POST':
        postform = DepartmentForm(request.POST, instance=department)
        if postform.is_valid():
            postform.save()
            return redirect('listdepartment')

    return render(request, 'depart_add_edit.html', {'dpform': form, 'name': 'Edit Department', 'edit': 'true', 'department': department})


def delDepartment(request, depid):
    if not request.user.is_authenticated:
        return redirect('login')

    department = Department.objects.get(id=depid)
    department.delete()
    return redirect('listdepartment')


def employeeList(request):
    if not request.user.is_authenticated:
        return redirect('login')

    employees = Employee.objects.all()
    return render(request, 'employee.html', {'name': 'Employees List', 'EmList': employees})


def addEmployee(request):
    if not request.user.is_authenticated:
        return redirect('login')

    form = EmployeeForm()
    if request.method == 'POST':

        postform = EmployeeForm(request.POST)
        if postform.is_valid():
            postform.save()
            return redirect('listEmployees')

    return render(request, 'emp_add_edit.html', {'empform': form, 'name': 'Add Employee', })


def editEmployee(request, empid):
    if not request.user.is_authenticated:
        return redirect('login')

    employee = Employee.objects.get(id=empid)
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        postform = EmployeeForm(request.POST, instance=employee)
        if postform.is_valid():
            postform.save()
            return redirect('listEmployees')

    return render(request, 'emp_add_edit.html', {'empform': form, 'name': 'Edit Employee', 'edit': 'true', 'employee': employee})


def delEmployee(request, empid):
    if not request.user.is_authenticated:
        return redirect('login')

    employee = Employee.objects.get(id=empid)
    employee.delete()
    return redirect('listEmployees')

# def oneemployee(request, empid):
#     employee = Employee.objects.get(id=empid)
#     return render(request, 'view_emp.html', {'employee': employee})
