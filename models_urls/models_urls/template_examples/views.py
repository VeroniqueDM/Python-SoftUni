# Create your views here.

from django.shortcuts import render
from django import forms
from models_urls.employees.models import Employees, Department


def templates_examples(request):
    pass

def index(request):
    employees_ = [e for e in Employees.objects.order_by('first_name','-last_name')],
    context = {

        'number_1':123,
        'number_2':321,
        'number_3': 200,
        'numbers':[123,321,200],
        'title': "EmployEes LiSt",
        'employees': [e for e in Employees.objects.order_by('department__name','first_name','-last_name')],
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'department_names': [d.name for d in Department.objects.all()],
        'filesize': 103873389,

    }
    return render(request, 'template_examples/index_templates.html', context)
