from django import template
import datetime

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.filter(name='cut_string')
def cut_string(value, arg: int):
    """Removes all values of arg from the given string"""
    return f"{value[0:arg]}..."


@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')