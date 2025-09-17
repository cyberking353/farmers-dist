from django.contrib import admin
from .models import Farm, Crop

@admin.register(Farm)
class FarmAdmin(admin.ModelAdmin):
    list_display = ("id", "farmer", "area_ha", "primary_crop", "secondary_crop")



@admin.register(Crop)
class CropAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")
    search_fields = ("name", "code")
