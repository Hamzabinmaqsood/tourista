from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    travel_style = models.CharField(max_length=50, blank=True)

    # New fields for onboarding data:
    budget = models.CharField(
        max_length=20,
        choices=[
            ('low', 'Low (< $500)'),
            ('medium', 'Medium ($500–$1,500)'),
            ('high', 'High (> $1,500)'),
        ],
        blank=True,
        help_text="User’s selected budget range"
    )
    duration = models.CharField(
        max_length=20,
        choices=[
            ('weekend', 'Weekend (1–2 days)'),
            ('week',    'Week (3–7 days)'),
            ('month',   'Month (8+ days)'),
        ],
        blank=True,
        help_text="User’s trip duration preference"
    )
    languages = models.CharField(
        max_length=200,
        blank=True,
        help_text="Comma-separated list of languages the user speaks"
    )

    # (existing groups/permissions overrides, etc.)

    
    def __str__(self):
        return f"{self.username} ({self.email})"
    
    class Meta:
        default_related_name = 'custom_users'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )