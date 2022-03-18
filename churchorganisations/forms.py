from django import forms

from churchorganisations.models import ChurchOrganisation


class ChurchOrganisationForm(forms.ModelForm):
    class Meta:
        model = ChurchOrganisation
        fields = "__all__"

        widgets = {
            "organisation_name": forms.TextInput(attrs={'class': 'form-control'}),
            "organisation_description": forms.Textarea(attrs={'class': 'form-control'}),
        }
