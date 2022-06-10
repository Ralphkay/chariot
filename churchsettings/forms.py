from django import forms

from churchsettings.models import ChurchSettings, ChurchSetup


class ChurchSetupForm(forms.ModelForm):
    class Meta:
        model = ChurchSetup
        fields = "__all__"

        widgets = {
            'user': forms.HiddenInput(),
            'church_name': forms.TextInput(attrs={'class': 'form-control'}),
            'short_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),

        }