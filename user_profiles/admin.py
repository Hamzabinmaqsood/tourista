from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone_number', 'travel_style')
    search_fields = ('username', 'email')
    list_filter = ('travel_style',)