import random

from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
#
# def home(request):
#     html = f'{request.method}: This is home'
#     if request.method == 'POST':
#         return HttpResponse(
#             html,
#             status=201,
#         )
#     elif request.method == 'GET':
#
#         return HttpResponse(
#             html,
#             content_type = 'text/plain',
#             # headers = {'x-vera-header': 'Django'},
#         )
#     else:
#         return HttpResponse('This is home')
from django.urls import reverse_lazy

from employees_app.employees.models import Department, Employee


def validate_positive(value):
    if value < 0:
        raise ValidationError('Value Must be positive')

#
# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#         label='Enter first name',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control-sm',
#                 # 'disabled':True,
#                 # 'readonly': 'Type first name',
#
#             }
#         )
#     )
#     last_name = forms.CharField(
#         max_length=40,
#         # null=True,
#         # blank=True,
#     )
#     egn = forms.CharField(
#         max_length=10,
#         # unique=True,
#     )
#     job_title = forms.ChoiceField(
#             choices=(
#                 (1, 'Python Dev'),
#                 (2, 'QA Engineer'),
#                 (3, 'DevOps Specialist'),
#             ),
#         )
#
#     company = forms.ChoiceField(
#
#         choices=((c, c) for c in Employee.COMPANIES),
#     )
#     age = forms.IntegerField(
#         # required=False,
#         # widget=forms.TextInput(
#         #     attrs={
#         #         # 'type': 'range',
#         #         # 'class': 'form-control',
#         #     }
#         # ),
#         validators=(
#             validate_positive,
#
#         )
#     )
#
class EmployeeForm(forms.ModelForm):
    # age = forms.IntegerField(
    #     validators=(
    #         validate_positive,
    #     )
    # )

    class Meta:
        model = Employee
        # fields = ('first_name', 'last_name', 'egn',)
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
              attrs={'class':'form-control'}
            ),
            'last_name': forms.TextInput(
                attrs={'class':'form-control'}
            ),
        }


class EmployeeOrderForm(forms.Form):
    order_by = forms.ChoiceField(
        choices=(
            ('first_name', 'First name'),
            ('last_name','Last name'),
        ),
        # required=False,
    )

class EditEmployeeForm(EmployeeForm):
    def clean(self):
        return super().clean()
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
           'egn': forms.TextInput(
               attrs={'readonly':'readonly'}
           )
        }
def create_employee(request):
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES)
        if employee_form.is_valid():
            # IF A MODELFORM IS USED, IT IS ENOUGH
            # TO SAY HERE:
            employee_form.save()
            # IF A NORMAL FORM IS USED:
            #
            # emp = Employee(
            #     first_name=employee_form.cleaned_data['first_name'],
            #     last_name=employee_form.cleaned_data['last_name'],
            #     egn=employee_form.cleaned_data['egn'],
            #     job_title_t=employee_form.cleaned_data['job_title_t'],
            #     company=employee_form.cleaned_data['company'],
            #     department_id=1,
            # )
            # SAME BUT SHORTER
            # emp = Employee(
            #     **employee_form.cleaned_data,
            #     department_id=1,
            # )
            # emp.save()
            return redirect('index')
    else:
        employee_form = EmployeeForm()
    employee_order_form = EmployeeOrderForm(request.GET)
    employee_order_form.is_valid()
    order_by = employee_order_form.cleaned_data.get('order_by', 'first_name')
    context = {
        'employee_form': employee_form,
        'employees': Employee.objects.order_by(order_by).all(),
        'employee_order_form': employee_order_form,
    }
    return render(request, 'create.html', context)


def edit_employee(request, pk):
    employee = Employee.objects.get(pk=pk)
    if request.method == 'POST':
        employee_form = EmployeeForm(request.POST, request.FILES, request.FILES,instance=employee)
        if employee_form.is_valid():
            employee_form.save()
    else:
        employee_form = EmployeeForm(instance=employee)
    context= {
    'employee': employee,
    'employee_form':employee_form,
    }
    return render(request, 'edit.html', context)
# def create_employee(request):
#     # GET / SHOW FORM
#     if request.method == 'GET':
#         context = {
#         'employee_form': EmployeeForm(),
#         }
#         return render(request, 'create.html', context)
#     # SAVE DATA
#     else:
#
#         employee_form = EmployeeForm(request.POST)
#         if employee_form.is_valid():
#             return redirect('index')
#         context={
#             'employee_form':employee_form,
#         }
#         return render(request, 'create.html', context)
    #
    # print(request.GET)
    # pass


def home(request):
    # print(reverse_lazy('index'))
    # print(reverse_lazy('go to home'))
    # print(reverse_lazy('list departments'))
    # print(reverse_lazy('department details', kwargs={
    #     'id': 1
    #
    # }))
    # rand_num = random.randint(0, 100)
    # context = {
    #     'employee_form': EmployeeForm(),
    #     'number': rand_num,
    #     'numbers': [random.randint(0, 100) for _ in range(5)]
    # }
    # return render(request, 'index.html', context,)
    return render(request, 'index.html')


def redirect_to_home(request):
    return redirect(to='index')
    # return redirect('department details',
    #     id=random.randint(0,100)
    # )


def not_found(request):
    # return HttpResponseNotFound()
    raise Http404()


def department_details(request, id):
    return HttpResponse(f'This is Department {id}')


def list_departments(request):
    # Option 1
    department = Department(
        name=f'Department {random.randint(1,20)}',
    )
    department.save()
    # Option 2
    Department.objects.create(
        name=f'Department {random.randint(1, 20)}',
    )
    # '''
    # Both options create a new Department
    # every time you reload the page
    # '''
    context = {
        # 'departments': Department.objects.filter(name__endswith='app'),
        # 'departments': Department.objects.prefetch_related('employee_set'),

        'departments': Department.objects.all(),
        'employees': Employee.objects.all(),
    }
    return render(request, 'list_departments.html', context)


def create_department(request):
    return HttpResponse('Created...')
