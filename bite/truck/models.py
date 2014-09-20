from django.db import models
from location.models import Location


class Truck(models.Model):
    name = models.CharField(max_length=255, null=True, unique=True)
    location = models.ForeignKey(Location, null=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False, null=False)
    last_update = models.DateTimeField(auto_now_add=True, auto_now=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'truck'