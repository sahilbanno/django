from django import template

register = template.library()

@register.filter(name='cut')
def cut(value, arg):
    """
        this cuts out all values of args from the string
    """
    return value.replace(arg,'')

# register.filter('cut', cut)
