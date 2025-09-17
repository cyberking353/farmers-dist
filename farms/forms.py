from django import forms
from .models import Farm

class FarmForm(forms.ModelForm):
    class Meta:
        model = Farm
        fields = ["farmer", "centroid_point", "polygon_geom", "area_ha", "primary_crop", "secondary_crop", "photos"]
