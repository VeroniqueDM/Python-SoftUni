from django import template

from models_urls.employees.models import Department

register = template.Library()

@register.inclusion_tag('tags/departments_list.html') #path
def departments_list():
    deps = Department.objects.prefetch_related('employees_set').all()
    #context
    return {
        'departments': deps,
    }