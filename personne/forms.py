from django import forms
from .models import Personne

class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['nom_personne', 'prenom_personne', 'telephone', 'image_personne']

    