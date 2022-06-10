from django import forms

from donations.models import MemberMonetaryDonation, MemberItemDonation, MonetaryDonation


class MonetaryDonationForm(forms.ModelForm):
    class Meta:
        model = MonetaryDonation
        fields = "__all__"

        widgets = {
            'donor': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'summernote'}),
        }


class MemberMonetaryDonationForm(forms.ModelForm):
    class Meta:
        model = MemberMonetaryDonation
        fields = "__all__"

        widgets = {
            'member': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'id': 'summernote', 'rows': 5}),
            'amount_donated': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),

        }


class MemberItemDonationForm(forms.ModelForm):
    class Meta:
        model = MemberItemDonation
        fields = "__all__"

        widgets = {
            'member': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'summernote', 'rows': 5}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),

        }