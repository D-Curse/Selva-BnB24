from django import forms
from .models import Ranger

class RangerForm(forms.ModelForm):
    class Meta:
        model = Ranger
        fields = ['name']