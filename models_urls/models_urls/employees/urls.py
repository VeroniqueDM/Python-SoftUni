from django.urls import path

from models_urls.employees.views import create_employee, edit_employee

# department_details, list_departments, not_found, create_department,



urlpatterns = [

    # path('<int:id>/', department_details, name= 'department details'), # if this is string, it won't reach the next path -> solution is to change order, this is why ORDER matters
    # # path('create/', create_department, name='create dep'),
    # path('', list_departments, name = 'list departments'),
    # path('filter/by/order-by/', list_departments, name = 'custom url'),
    # path('not-found/', not_found),
    path('create/', create_employee, name='create employee'),
    path('edit/<int:pk>/', edit_employee, name='edit employee')

]