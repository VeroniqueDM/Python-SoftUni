"""models_urls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from models_urls.employees.views import home, create_employee
#department_details, list_departments, go_to_home, create_department, \


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='index'),
    path('employees/', include('models_urls.employees.urls')),
    # path('create/', create_employee, name='create employee'),
]

#     # path('departments/1/', department_details),
#     # path('departments/',include('models_urls.employees.urls')),
#     path('go-to-home/', go_to_home, name = 'go to home'),
#     path('templates/', include('models_urls.template_examples.urls')),
#     path('employees/', include('models_urls.employees.urls')),
#     path('create/', create_employee, name='create employee')
#
#     # path('departments/', include('models_urls.employees.urls')),
# ]
