from django.db import models

# Create your models here.


class Location(models.Model):
    longitude = models.CharField(max_length=255, null=True)
    latitude = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False, null=False)
    last_update = models.DateTimeField(auto_now_add=True, auto_now=True, null=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'location'
        unique_together = ('longitude', 'latitude')
