from django.db import models

class CatalogoDireccion(models.Model):
    country = models.CharField(max_length=30)
    state_id = models.CharField(max_length=5)
    state_name = models.CharField(max_length=50)
    city_base = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=15)

    class Meta:
        unique_together = ('country', 'state_id', 'state_name', 'city_base', 'city', 'zipcode')

    def __str__(self):
        return f"{self.country} - {self.state_id} - {self.state_name} - {self.city_base} - {self.city} - {self.zipcode}"

