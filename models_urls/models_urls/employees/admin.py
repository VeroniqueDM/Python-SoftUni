from django.contrib import admin

# Register your models here.

from models_urls.employees.models import Employees, Department


@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
        list_display = ('id', 'first_name', 'last_name', 'job_title', 'department')
    # pass

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
        list_display = ('id', 'name', 'created_on', 'updated_on')