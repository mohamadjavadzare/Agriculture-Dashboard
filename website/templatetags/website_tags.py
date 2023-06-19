from django import template
from website.models import *
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def upto(value, delimiter=None):
    return value.split(delimiter)[0]
upto.is_safe = True

@register.inclusion_tag('dashboard.html', name='done_taskss')
def done_tasks():
    done = Project.objects.filter(completion=100)
    count_done = done.count()
    if count_done == 0:
        count_done = "zero"
    # cat_dict = {}
    # categories = Category.objects.all()
    # for name in categories:
    #     cat_dict[name] = name
    return { 'count_done_tasks':count_done }

@register.simple_tag
def available_workers():
    workers = Worker.objects.filter(status=True).count()
    return workers