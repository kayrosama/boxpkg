import csv
from django.core.management.base import BaseCommand
from backend.models.catalogos import CatalogoDireccion

class Command(BaseCommand):
    help = 'Carga los datos del catálogo de direcciones desde uszips.csv'

    def handle(self, *args, **kwargs):
        path = 'static/xfile/uszips.csv'
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            count = 0
            for row in reader:
                obj, created = CatalogoDireccion.objects.get_or_create(
                    country=row['COUNTRY'],
                    state_id=row['STATE_ID'],
                    state_name=row['STATE_NAME'],
                    city_base=row['CITY_BASE'],
                    city=row['CITY'],
                    zipcode=row['ZIPCODE']
                )
                if created:
                    count += 1
            self.stdout.write(self.style.SUCCESS(f'Se cargaron {count} registros nuevos.'))
