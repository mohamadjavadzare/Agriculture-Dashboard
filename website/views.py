from django.shortcuts import render
import requests
from decouple import config
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
    api_key = config(
        "openweather_apikey", default="18f933ce846bc85b1007e70e217290fe"
    )
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?lat=37.474806&lon=57.315210&appid={api_key}"
    )
    data = response.json()
    # convert from kelvin to celsius with 0.01 rounding
    data["main"]["temp"] = round(data["main"]["temp"] - 273.15, 2)
    data["main"]["feels_like"] = round(
        data["main"]["feels_like"] - 273.15, 2
    )
    data["main"]["temp_min"] = round(data["main"]["temp_min"] - 273.15, 2)
    data["main"]["temp_max"] = round(data["main"]["temp_max"] - 273.15, 2)
    content = {"weather": data}
    return render(request, 'weather.html', content)