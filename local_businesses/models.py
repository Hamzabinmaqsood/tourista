from django.db import models

class LocalBusiness(models.Model):
    BUSINESS_TYPES = [
        ('HOTEL', 'Hotel'),
        ('RESTAURANT', 'Restaurant'),
        ('ATTRACTION', 'Tourist Attraction'),
    ]
    
    name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=20, choices=BUSINESS_TYPES)
    location = models.CharField(max_length=200)
    sustainability_score = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name

    PRICE_TIERS = [
        ('low', 'Low (< $500)'),
        ('medium', 'Medium ($500–$1,500)'),
        ('high', 'High (> $1,500)'),
    ]
    price_tier = models.CharField(
        max_length=10,
        choices=PRICE_TIERS,
        default='medium',
        help_text="Business price tier for budget filtering"
    )