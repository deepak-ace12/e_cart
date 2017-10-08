from django import forms
from .models import Quantity, Adjustment


class QuantityForm(forms.ModelForm):

    class Meta:
        model = Quantity
        fields = ('quantity',)


class AdjustmentForm(forms.ModelForm):
    notes = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': "Add a Note",
            'rows': 3,
            'style': 'resize:none;',

        }
    ))

    class Meta:
        model = Adjustment
        fields = ('amount', 'notes',)
