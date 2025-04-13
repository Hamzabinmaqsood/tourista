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