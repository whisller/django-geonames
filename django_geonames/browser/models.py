from django.db import models


class City(models.Model):
    class Meta:
        db_table = 'cities'

    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    country_code = models.CharField(max_length=255)
