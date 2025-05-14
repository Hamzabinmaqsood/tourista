from django.core.management.base import BaseCommand
from frontend.models import TripPackage

class Command(BaseCommand):
    help = "Load 5 dummy TripPackage entries"

    def handle(self, *args, **options):
        packages = [
            {
                "title": "Kashmir Lakes Tour",
                "duration": 7,
                "price": 500,
                "description": "Explore Dal, Wular & Manasbal lakes with guided boat rides."
            },
            {
                "title": "Hunza Valley Trek",
                "duration": 5,
                "price": 450,
                "description": "Trek through Karimabad, Attabad Lake & Passu Cones."
            },
            {
                "title": "Naran & Kaghan Expedition",
                "duration": 4,
                "price": 300,
                "description": "Visit Saif-ul-Maluk, Babusar Top & Kaghan’s villages."
            },
            {
                "title": "Skardu Adventure",
                "duration": 6,
                "price": 550,
                "description": "Discover Deosai Plains, Shangrila Resort & Shigar Fort."
            },
            {
                "title": "Murree Hill Retreat",
                "duration": 2,
                "price": 150,
                "description": "Weekend pine-forest getaway with Mall Road & chairlifts."
            },
        ]
        for pkg_data in packages:
            obj, created = TripPackage.objects.get_or_create(
                title=pkg_data["title"],
                defaults=pkg_data
            )
            status = "Created" if created else "Already exists"
            self.stdout.write(f"{status}: {obj.title}")
