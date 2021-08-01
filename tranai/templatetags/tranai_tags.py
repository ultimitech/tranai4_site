from django import template
from django.conf import settings
from ..models import Task
from crum import get_current_user
# import crum

register = template.Library()

User = settings.AUTH_USER_MODEL

# @register.assignment_tag
@register.simple_tag
def get_current_user_active_tasks():
    current_user = get_current_user()
    # return Task.objects.filter(user=current_user).filter(active=True).order_by('translation__lan', 'translation__document__descriptor')
    return Task.objects.filter(user=current_user).filter(active=True).order_by('translation__lan')
