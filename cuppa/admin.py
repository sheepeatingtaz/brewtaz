from django.contrib import admin

# Register your models here.
from cuppa.models import Brew, Tea


@admin.register(Brew)
class BrewAdmin(admin.ModelAdmin):
    list_display = ('name', 'beverage', 'milk', 'sugars', 'notes', 'created_at')
    list_filter = ['created_at', 'name', 'beverage']
    search_fields = ['name']

@admin.register(Tea)
class TeaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ['name']
    search_fields = ['name']
