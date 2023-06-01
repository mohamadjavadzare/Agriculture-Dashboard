from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    list_display = ('name','phone','status', 'last_employed')
    search_fields = ('status',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    list_display = ('name','completion','budget',)
    search_fields = ('status',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    list_display = ('name','completion','budget','status')
    search_fields = ('status',)

admin.site.register(ProductStatus)

@admin.register(Tools)
class ToolsAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-'
    list_display = ('name','number','status')
    search_fields = ('status',)

admin.site.register(ToolsStatus)
