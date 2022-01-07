from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from rest_framework import viewsets
import requests

from .models import Employee
from .forms import EmployeeForm
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


def home(request):
    response = requests.get('http://localhost:8000/api/employees/')
    data = response.json()
    form = EmployeeForm
    return render(request, 'home.html', {'employees': data, 'form': form})


def create_employee(request):
    response = requests.post('http://localhost:8000/api/employees/', data=request.POST)
    return redirect('home')


def update_employee(request, *args, **kwargs):
    employee = Employee.objects.get(id=kwargs.get('pk'))
    if request.method == 'GET':
        form = EmployeeForm(instance=employee)
        return HttpResponse(form.as_p())
    elif request.method == 'POST':
        requests.put(f'http://localhost:8000/api/employees/{employee.pk}/', data=request.POST)
        return redirect('home')
# Create your views here.
