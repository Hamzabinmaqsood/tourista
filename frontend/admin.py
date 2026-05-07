from django.contrib import admin
from .models import TripPackage, Trip, CustomUser, Itinerary
from django.contrib.auth.admin import UserAdmin

@admin.register(TripPackage)
class TripPackageAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    search_fields = ('title',)


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'created_at')
    list_filter  = ('status', )


@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')


# If you want to manage CustomUser via the admin:
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Extra Info', {
            'fields': ('phone_number', 'travel_style'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Extra Info', {
            'fields': ('phone_number', 'travel_style'),
        }),
    )
