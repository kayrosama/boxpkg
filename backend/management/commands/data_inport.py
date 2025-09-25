import os
import csv
from django.core.management.base import BaseCommand
from backend.models import State, Country, ZipCode  # Ajusta este import según tu estructura

class Command(BaseCommand):
    help = 'Importa estados, condados y códigos postales desde archivos CSV en el subdirectorio "datos".'

    def handle(self, *args, **kwargs):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        datos_dir = os.path.join(base_dir, 'datos')

        # Importar estados
        states_path = os.path.join(datos_dir, 'us_states.csv')
        if not os.path.exists(states_path):
            self.stdout.write(self.style.ERROR(f"Archivo no encontrado: {states_path}"))
            return

        with open(states_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                State.objects.get_or_create(abbr=row['abbr'], name=row['name'])

        # Importar condados
        countries_path = os.path.join(datos_dir, 'us_countries.csv')
        if not os.path.exists(countries_path):
            self.stdout.write(self.style.ERROR(f"Archivo no encontrado: {countries_path}"))
            return

        with open(countries_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                state = State.objects.filter(abbr=row['state']).first()
                if state:
                    Country.objects.get_or_create(name=row['name'], state=state)

        # Importar códigos postales
        zipcodes_path = os.path.join(datos_dir, 'us_zipcodes.csv')
        if not os.path.exists(zipcodes_path):
            self.stdout.write(self.style.ERROR(f"Archivo no encontrado: {zipcodes_path}"))
            return

        with open(zipcodes_path, newline='', encoding='utf-8') as csvfile:
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
                    lat=float(row['lat']) if row['lat'] else None,
                    lon=float(row['lon']) if row['lon'] else None
                )

        self.stdout.write(self.style.SUCCESS('✅ Datos importados correctamente.'))

