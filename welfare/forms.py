from django.forms import forms

from welfare.models import WelfareMembershipLevy


class WelfareMembershipLevy(forms.ModelForm):
    class Meta:
        model = WelfareMembershipLevy
        fields = ('member', 'year', 'month', 'month_levy_paid')

    widgets = {
        'member': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
        'month': forms.Select(attrs={'class': 'form-control'}),
        'year': forms.Select(attrs={'class': 'form-control'}),
        'month_levy_paid': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
    }
