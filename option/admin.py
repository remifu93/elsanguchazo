from django.contrib import admin
from .models import Option

@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'recommended',)
    list_filter = ('category__name', 'recommended')
    search_fields = ('name', 'category__name', 'price', 'description')