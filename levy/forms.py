
from django import forms
from django.core.exceptions import ValidationError

from levy.models import Levy
from levy.validators import validate_monthly_levy_paid


class LevyForm(forms.ModelForm):
    month_levy_paid = forms.CharField(validators=[validate_monthly_levy_paid],
                                      widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0}))

    class Meta:
        model = Levy
        fields = "__all__"

        widgets = {
            'member': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'month': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            # 'month_levy_paid': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }