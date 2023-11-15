from django.urls import path

from employees_app.employees.views import department_details, list_departments, not_found, redirect_to_home, \
    create_department, create_employee, edit_employee

urlpatterns = [
    # path('create/', create_department),
    path('create/', create_employee, name='create employee'),
    path('edit/<int:pk>/', edit_employee, name='edit employee'),
    path('<id>/', department_details, name='department details'),
    path('', list_departments, name='list departments'),
    path('not-found/', not_found),


]