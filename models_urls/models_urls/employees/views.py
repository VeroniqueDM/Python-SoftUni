#import  random

# Create your views here.
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
# from django.urls import reverse_lazy
#from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect

from models_urls.employees.models import Department, Employees
def validate_positive(value):
    if value<0:
        raise ValidationError('Value must be positive')

# class EmployeeForm(forms.Form):
#     first_name = forms.CharField(
#         max_length=30,
#         label= "Enter first Name",
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#         }
#     ),
#     )
#     last_name = forms.CharField(
#         max_length=40,
#         widget=forms.TextInput(attrs={
#
#             'class': 'form-control',
#         })
#
#
#     )
#     age = forms.IntegerField(
#         required=False,
#         widget=forms.TextInput(attrs={
#             # 'type':'range',
#             # 'type':'number',
#             'class': 'form-control',#from the bootstrap,
#
#         }
#     ),
#         validators=(
#             validate_positive,
#         ),
#          #my own validator ^^
#     )
#     egn = forms.CharField(
#         max_length=10,
#
#         # unique=True,
#         # null=True,
#         # verbose_name='EGN'
#
#     )
#     job_title = forms.ChoiceField(
#          choices=(
#              (1, 'Software Engineer'),
#              (2, 'Dev Ops'),
#              (3, 'QA')
#          ),
#      )
    # company_name = forms.ChoiceField(
    #     max_length=max(len(c) for c in Employees.COMPANIES),
    #     choices= ((c, c) for c in Employees.COMPANIES))

    # department = forms.ForeignKey(
    #     Department,
    #     on_delete=forms.CASCADE,
    #     null=True
    # )


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employees
        fields = '__all__'
        # fields = ('first_name', 'last_name', 'egn')
        # widgets = {}
class EmployeeOrderForm(forms.Form):
    order_by = (
        ('first_name', 'First name'),
        ('last_name', 'Last name'),
    )
    required = False
class EditEmployeeForm(EmployeeForm):
    # def clean_egn(self):
    def clean(self):
        return super().clean()
    class Meta:
        model= Employees
        fields = '__all__'
        widgets = {
            'egn': forms.TextInput(
                attrs={'readonly': 'readonly'}
            )
        }

def home(request):
    # print(reverse_lazy('index'))
    # print(reverse_lazy('go to home'))
    # print(reverse_lazy('list departments'))
    # print(reverse_lazy('custom url'))
    # print(reverse_lazy('department details', kwargs = {'id':1, }))


    # rand_num = random.randint(0,1024)
    # context= {
    #     'number': rand_num,
    #     'numbers': [random.randint(0,1024) for _ in range(10)],
    # 'employee_form': EmployeeForm(),
    # }
    # return render(request, 'index.html', context)
    context = {
        'employee_form': EmployeeForm(),
    }
    return render(request, 'index.html')
                  #, context)
def create_employee(request):
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST, request.FILES)
        if employee_form.is_valid():
            # emp = Employees(
            #             first_name=employee_form.cleaned_data['first_name'],
            #             last_name = employee_form.cleaned_data['last_name'],
            #             egn= employee_form.cleaned_data['egn'],
            #             job_title=employee_form.cleaned_data['job_title'],
            #             # company=employee_form.cleaned_data['company_name'],
            #             department_id=1,
            #         )
            # emp = Employees(**employee_form.cleaned_data, department_id=1,)
            # emp.full_clean() #explicit call validator for normal Forms. Not needed in model forms
            # emp.save()
            employee_form.save()
            return redirect('index')

    else:
        employee_form = EmployeeForm()

    employee_order_form= EmployeeOrderForm(request.GET)
    employee_order_form.is_valid()
    order_by = employee_order_form.cleaned_data.get('order_by', 'first_name') #from the class not here
    context = {
        'employee_form': employee_form,
        'employees': Employees.objects.order_by(order_by).all(),
        'employee_order_form': employee_order_form,

    }
    return render(request, 'create.html', context)

def edit_employee(request, pk):
    employee = Employees.objects.get(pk=pk)
    if request.method == "POST":
        employee_form = EditEmployeeForm(
            request.POST,
            request.FILES,
            instance=employee,
        )
        if employee_form.is_valid():
            employee_form.save()
    else:
        employee_form = EditEmployeeForm(instance=employee)
    context= {
        'employee': employee,
        'employee_form' : employee_form,
    }
    return render(request,'edit.html', context)


# def create_employee(request):
#     if request.method == "GET":
#         context = {
#             'employee_form': EmployeeForm(),
#
#             }
#         return render(request, 'create.html', context)
#     else:
#         employee_form = EmployeeForm(request.POST)
#         if employee_form.is_valid():
#             return redirect('index')
#         else:
#             context = {
#                 'employee_form': employee_form,
#
#             }
#             return render(request, 'create.html', context)
    # if request.method == 'POST':
    #     employee_form = EmployeeForm(request.POST)
    #     if employee_form.is_valid:
    #         # emp = Employees(
    #         #     first_name=employee_form.cleaned_data['first_name'],
    #         #     last_name = employee_form.cleaned_data['last_name'],
    #         #     egn= employee_form.cleaned_data['egn'],
    #         #     job_title=employee_form.cleaned_data['job_title'],
    #         #     # company=employee_form.cleaned_data['company_name'],
    #         #     department_id=1,
    #         # )
    #         # emp = Employees(**employee_form.cleaned_data, department_id=1,)
    #         # emp.save()
    #         return redirect('index')
    #     # if not valid => not working?
    # else:
    #     employee_form = EmployeeForm()
    # context = {
    #     'employee_form': employee_form,
    #
    #     }
    # return render(request, 'create.html', context)
#
# def department_details(request, id):
#     return HttpResponse(f'This is department {id}, {type(id)}')
#
# def list_departments(request):
#     department = Department(
#         name=f'Department {random.randint(1,1024)}',
#     )
#     # department.save()
#     # or use this, saves directly \/
#     Department.objects.create(
#         name=f'Department {random.randint(1, 1024)}',
#     )
#     context = {
#         'departments': Department.objects.all(),
#         'filtered_deps': Department.objects.filter(name='HR'),
#         # 'other_filter': Department.objects.filter(name__in=), ->> there are many other options to filter by name etc.
#         'employees': Employees.objects.all(),
#     }
#     return render(request, 'list_departments.html', context)

# def not_found(request):
#     return HttpResponseNotFound()
#
# def go_to_home(request):
#     return redirect('index')
#     # return redirect('department details', id=random.randint(1,1024))
#
# def create_department(request):
#     return HttpResponse('Created')
