from django import forms

from offerings.models import Offering, OfferingType


class OfferingForm(forms.ModelForm):
    class Meta:
        model = Offering
        fields = "__all__"

        widgets = {
            'service': forms.Select(attrs={'class': 'form-control'}),
            'type_of_offering': forms.Select(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'id': 'summernote'}),
        }


class OfferingTypeForm(forms.ModelForm):
    class Meta:
        model = OfferingType
        fields = "__all__"

        widgets = {
            'type_of_offering': forms.TextInput(attrs={'class': 'form-control'}),
        }