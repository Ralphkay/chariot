from django import forms

from pledges.models import MonetaryPledge, ItemPledge, MemberItemPledge, MemberMonetaryPledge


class MonetaryPledgeForm(forms.ModelForm):
    class Meta:
        model = MonetaryPledge
        fields = ['pledge_person', 'amount_pledged','email',
                  'amount_paid', 'phone_number', 'description']

        widgets = {
            'pledge_person': forms.TextInput(attrs={'class': 'form-control'}),
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'amount_pledged': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            'amount_paid': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'summernote'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


# class ItemPledgeForm(forms.ModelForm):
#     class Meta:
#         model = ItemPledge
#         fields = ['pledge_person', 'item', 'quantity_pledged',
#                   'quantity_redeemed', 'contact_information']
#
#         widgets = {
#             'pledge_person': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'on'}),
#             'item': forms.TextInput(attrs={'class': 'form-control'}),
#             'quantity_pledged': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
#             'quantity_redeemed': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
#             'description': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
#             'contact_information': forms.Textarea(attrs={'class': 'form-control'}),
#         }
#

class MemberMonetaryPledgeForm(forms.ModelForm):
    class Meta:
        model = MemberMonetaryPledge
        fields = ['pledge_person', 'amount_pledged', 'amount_paid']

        widgets = {
            'pledge_person': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'amount_pledged': forms.TextInput(attrs={'class': 'form-control','type': 'number', 'step': 'any'}),
            'amount_paid': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': 'any'}),
            # 'description': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            # 'contact_information': forms.Textarea(attrs={'class': 'form-control'}),
        }


class MemberItemPledgeForm(forms.ModelForm):
    class Meta:
        model = MemberItemPledge
        fields = ['pledge_person', 'item', 'quantity_pledged',
                  'quantity_redeemed', 'phone_number', 'email']

        widgets = {
            'pledge_person': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity_pledged': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'quantity_redeemed': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'type': 'number'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }