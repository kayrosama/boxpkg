from django.db import models

class State(models.Model):
    abbr = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='countries')

    def __str__(self):
        return f"{self.name}, {self.state.abbr}"

class ZipCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, related_name='zipcodes')
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, related_name='zipcodes')
    area_code = models.CharField(max_length=10, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.code} - {self.city}"
