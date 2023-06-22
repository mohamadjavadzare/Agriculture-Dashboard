from django.shortcuts import render
from .models import *
# Create your views here.

from django.contrib.auth.decorators import login_required

@login_required
def dashboard_view(request, *args, **kwargs):
    projects = Project.objects.all()
    done_projects = Project.objects.filter(completion=100).count()
    context = {'projects':projects , 'done_projects':done_projects}
    return render(request, 'dashboard.html', context)

@login_required
def billing_view(request, *args, **kwargs):
    cards = Card.objects.all()
    context = {'cards':cards}
    return render(request, 'billing.html', context)

@login_required
def notifications_view(request, *args, **kwargs):
    return render(request, 'notifications.html')

@login_required
def tables_view(request, *args, **kwargs):
    workers = Worker.objects.all()
    products = Product.objects.all()
    tools = Tools.objects.all()
    context = {'workers': workers , 'products': products , 'tools': tools}
    return render(request, 'tables.html', context)

@login_required
def weather_view(request, *args, **kwargs):
    return render(request, 'weather.html')