from django.forms import ModelForm, TextInput, Textarea, Select, DateInput
from . models import Department, Employee


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': "form-control forms-fonts",
            }),
            'description': Textarea(attrs={
                'class': "form-control forms-fonts",
            }),

        }


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'firstnme': TextInput(attrs={
                'class': "form-control forms-fonts",
            }),
            'lastname': TextInput(attrs={
                'class': "form-control forms-fonts",
            }),
            'department': Select(attrs={
                'class': "form-select forms-fonts",
            }),
            'createdby': Select(attrs={
                'class': "form-select forms-fonts",
            }),
            'salary': TextInput(attrs={
                'class': "form-control forms-fonts",
            }),
            'address': TextInput(attrs={
                'class': "form-control forms-fonts",
            }),
            'doj': DateInput(attrs={
                'class': "form-control forms-fonts", 'type': 'date'
            }),


        }
