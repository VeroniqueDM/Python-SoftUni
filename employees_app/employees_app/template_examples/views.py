from django.shortcuts import render

# Create your views here.
from employees_app.employees.models import Employee, Department


def index(request):
    context = {
        'number_1': 123,
        'number_2': '321',
        'numbers' : [123, 321, 200],
        'title':'Employees list',
        'employees': Employee.objects.order_by('department__name','last_name','-first_name').all(),
        'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'department_names': [d.name for d in Department.objects.all()]
    }
    return render(request, 'templates_examples/index.html', context)