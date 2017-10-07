from django import forms
from .models import Quantity, Adjustment


class QuantityForm(forms.ModelForm):

    class Meta:
        model = Quantity
        fields = ('quantity',)


class AdjustmentForm(forms.ModelForm):

    class Meta:
        model = Adjustment
        fields = ('amount',)