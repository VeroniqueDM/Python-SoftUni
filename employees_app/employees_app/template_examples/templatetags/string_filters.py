from django import template

register = template.Library()

@register.filter(name = 'capitalize')
def capitalize(value):
    """
    This is a filter that Capitalizes the first letter of the value.
    THIS IS text -> This is text
    """
    value = str(value)
    return value[0].upper() + value[1:].lower()