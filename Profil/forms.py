from django import forms
from .models import Citoyen,Reclamation
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CitoyenForm(forms.ModelForm):
    def clean_date_naissance(self):
        date_naissance = self.cleaned_data['date_naissance']
        if date_naissance > timezone.now().date():
            raise forms.ValidationError("La date de naissance ne peut pas être supérieure à la date d'aujourd'hui.")
        return date_naissance
    class Meta:
        model=Citoyen
        fields=['date_naissance','adresse','telephone','cin']


class ReclamationForm(forms.ModelForm):
    class Meta:
        model = Reclamation
        fields = ['nom', 'date_reclamation', 'description', 'symptomes', 'date_effets_secondaires']

    
