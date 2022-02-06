
from django import forms
from.models import Location

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('loc_statut', 'loc_cli_id', 'loc_date_fin','loc_date_debut', 'loc_vel_id', 'loc_num')
