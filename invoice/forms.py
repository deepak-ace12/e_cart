from django import forms
from .models import Quantity


class QuantityForm(forms.ModelForm):

    class Meta:
        model = Quantity
        fields = ('quantity',)
