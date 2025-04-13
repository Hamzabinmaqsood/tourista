from django.contrib import admin
from .models import LocalBusiness

@admin.register(LocalBusiness)
class LocalBusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'business_type', 'location', 'sustainability_score')
    search_fields = ('name', 'business_type')
    list_filter = ('business_type', 'sustainability_score')