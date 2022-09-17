from django.db import models
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    firstnme = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.FloatField()
    doj = models.DateField()
    address = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstnme
