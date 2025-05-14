from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# ——————————————————————————————————————————————————————
# 1) Define your models
# ——————————————————————————————————————————————————————

class TripPackage(models.Model):
    title             = models.CharField(max_length=200)
    short_description = models.CharField(max_length=400)
    full_description  = models.TextField()
    price             = models.DecimalField(max_digits=8, decimal_places=2)
    image             = models.ImageField(upload_to='packages/', null=True, blank=True)

    def __str__(self):
        return self.title


class Trip(models.Model):
    STATUS_CHOICES = [
        ('draft',     'Draft'),
        ('booked',    'Booked'),
        ('completed', 'Completed'),
    ]
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    packages    = models.ManyToManyField(TripPackage, related_name='trips')
    status      = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s trip ({self.get_status_display()})"


class CustomUser(AbstractUser):
    TRAVEL_STYLE_CHOICES = [
        ('adventure', 'Adventure Travel'),
        ('luxury',    'Luxury Travel'),
        ('budget',    'Budget Travel'),
        ('family',    'Family Travel'),
    ]
    phone_number = models.CharField(max_length=20)
    travel_style = models.CharField(max_length=20, choices=TRAVEL_STYLE_CHOICES)

    def __str__(self):
        return self.username

class Itinerary(models.Model):
    user       = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name       = models.CharField(max_length=200)
    packages   = models.ManyToManyField(TripPackage, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"
