from django.db import models
from django.conf import settings

class Farm(models.Model):
    farmer = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="farms"
    )
    ## I just added this to test the map
    latitude = models.FloatField()
    longitude = models.FloatField()
    # Geo fields (to be integrated with Leaflet.js later)
    centroid_point = models.CharField(max_length=255, blank=True, null=True)  # store GPS point (lat,lon)
    polygon_geom = models.TextField(blank=True, null=True)  # store polygon JSON/WKT string for later Leaflet integration
    
    # Farm details
    area_ha = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    primary_crop = models.ForeignKey('Crop', related_name="primary_crop_farms", on_delete=models.SET_NULL, null=True, blank=True)
    secondary_crop = models.ForeignKey('Crop', related_name="secondary_crop_farms", on_delete=models.SET_NULL, null=True, blank=True)
    
    # Photos (optional)
    photos = models.ImageField(upload_to="farm_photos/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Farm of {self.farmer.username} - {self.primary_crop or 'No crop'}"

class Crop(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
