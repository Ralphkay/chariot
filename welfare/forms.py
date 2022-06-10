

from django import forms

from welfare.models import WelfareMembershipLevy, Welfare, WelfareContribution


class WelfareMembershipLevyForm(forms.ModelForm):
    class Meta:
        model = WelfareMembershipLevy
        fields = "__all__"

        widgets = {
            'member': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'month': forms.Select(attrs={'class': 'form-control'}),
            'year': forms.Select(attrs={'class': 'form-control'}),
            'month_welfare_paid': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }


class WelfareForm(forms.ModelForm):
    class Meta:
        model = Welfare
        fields = "__all__"

        widgets = {
            'welfare_title': forms.TextInput(attrs={'class': 'form-control'}),
            'welfare_description': forms.Textarea(attrs={'class': 'form-control'}),
            'deadline': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class WelfareContributionForm(forms.ModelForm):
    class Meta:
        model = WelfareContribution
        fields = "__all__"

        widgets = {
            'member': forms.TextInput(attrs={'type': 'hidden'}),
            'amount_contributed': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
        }