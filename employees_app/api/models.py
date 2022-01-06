from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=200)
    floor = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name} ({self.floor})'


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    age = models.PositiveIntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees')
    programming_language = models.ForeignKey(ProgrammingLanguage, on_delete=models.CASCADE, related_name='employees')

    class Meta:
        db_table = 'employees'

    def __str__(self):
        return f'{self.name} {self.last_name}'



# Create your models here.
