from django.contrib import admin

# Register your models here.
from cuppa.models import Brew


@admin.register(Brew)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'beverage', 'milk', 'sugars', 'notes', 'created_at')
    list_filter = ['created_at', 'name', 'beverage']
    search_fields = ['name']