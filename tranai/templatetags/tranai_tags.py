from django import template
from django.conf import settings
from ..models import Task

register = template.Library()

User = settings.AUTH_USER_MODEL

# @register.assignment_tag
@register.simple_tag
def get_active_tasks():
    #   tasks = Task.objects.filter(user=get_current_user)
    pass
