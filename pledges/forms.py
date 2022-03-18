from django import forms

from pledges.models import MonetaryPledge, MaterialPledge, MemberMaterialPledge, MemberMonetaryPledge


class MonetaryPledgeForm(forms.ModelForm):
    class Meta:
        model = MonetaryPledge
        fields = ['pledge_person', 'amount_pledged',
                  'amount_paid', 'contact_information']

        widgets = {
            'pledge_person': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'on'}),
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'amount_pledged': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            'amount_paid': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'contact_information': forms.Textarea(attrs={'class': 'form-control'}),
        }


class MaterialPledgeForm(forms.ModelForm):
    class Meta:
        model = MaterialPledge
        fields = ['pledge_person', 'item', 'quantity_pledged',
                  'quantity_redeemed', 'contact_information']

        widgets = {
            'pledge_person': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'on'}),
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity_pledged': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            'quantity_redeemed': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'contact_information': forms.Textarea(attrs={'class': 'form-control'}),
        }


class MemberMonetaryPledgeForm(forms.ModelForm):
    class Meta:
        model = MemberMonetaryPledge
        fields = ['pledge_person', 'amount_pledged',
                  'amount_paid', 'contact_information']

        widgets = {
            'pledge_person': forms.Select(attrs={'class': 'form-control', 'autocomplete': 'on'}),
            'amount_pledged': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            'amount_paid': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'contact_information': forms.Textarea(attrs={'class': 'form-control'}),
        }


class MemberMaterialPledgeForm(forms.ModelForm):
    class Meta:
        model = MemberMaterialPledge
        fields = ['pledge_person', 'item', 'quantity_pledged',
                  'quantity_redeemed', 'contact_information']

        widgets = {
            'pledge_person': forms.Select(attrs={'class': 'form-control', 'autocomplete': 'on'}),
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity_pledged': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'quantity_redeemed': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'contact_information': forms.Textarea(attrs={'class': 'form-control'}),
        }