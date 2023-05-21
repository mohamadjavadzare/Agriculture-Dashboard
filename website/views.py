from django.shortcuts import render

# Create your views here.

def dashboard_view(request, *args, **kwargs):
    return render(request, 'dashboard.html')

def billing_view(request, *args, **kwargs):
    return render(request, 'billing.html')

def notifications_view(request, *args, **kwargs):
    return render(request, 'notifications.html')

def tables_view(request, *args, **kwargs):
    return render(request, 'tables.html')

def weather_view(request, *args, **kwargs):
    return render(request, 'weather.html')