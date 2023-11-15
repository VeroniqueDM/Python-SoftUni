from django import template
register = template.Library()

@register.filter(name='capitalize')
def capitalize(value):
    """

    Capitalizes the value - first letter is cap, the rest is lowercase
    *THIS IS TEXT => This is text
    """
    value = str(value)
    return value[0].upper() + value[1:].lower()
