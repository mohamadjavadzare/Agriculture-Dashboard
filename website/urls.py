from django.urls import path
from website.views import *

app_name  = 'website'

urlpatterns = [
    path('' , dashboard_view, name='dashboard'),
    path('billing', billing_view, name='billing'),
    path('notifications', notifications_view , name='notifications'),
    path('tables', tables_view , name='tables'),
    path('weather', weather_view , name='weather'),
]
