import os
import csv
from django.core.management.base import BaseCommand
from backend.models import State, Country, ZipCode

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATOS_DIR = os.path.join(BASE_DIR, 'datos')


class Command(BaseCommand):
    help = 'Import US states, countries, and zip codes from CSV files'

    def handle(self, *args, **kwargs):
        # Import States
        path = os.path.join(DATOS_DIR, 'us_states.csv')
        if not os.path.exists(path):
            self.stdout.write(self.style.ERROR(f"Archivo no encontrado: {path}"))
            return

        with open('us_states.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                State.objects.get_or_create(abbr=row['abbr'], name=row['name'])

        # Import Countries
        with open('datos/us_countries.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                state = State.objects.filter(abbr=row['state']).first()
                if state:
                    Country.objects.get_or_create(name=row['name'], state=state)

        # Import ZipCodes
        with open('datos/us_zipcodes.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                state = State.objects.filter(abbr=row['state']).first()
                country = Country.objects.filter(name=row['country'], state=state).first()
                ZipCode.objects.get_or_create(
                    code=row['code'],
                    city=row['city'],
                    state=state,
                    country=country,
                    area_code=row['area_code'] if row['area_code'] else None,
                    lat=row['lat'] if row['lat'] else None,
                    lon=row['lon'] if row['lon'] else None
                )

        self.stdout.write(self.style.SUCCESS('Data imported successfully.'))
        
