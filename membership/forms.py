from django import forms

from membership.models import Member, MemberReligiousCV


class MembershipForm(forms.ModelForm):
    # profile_photo = forms.ImageField()

    class Meta:
        model = Member
        fields = '__all__'

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'middle_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.RadioSelect(),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'your@example.com'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'primary_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'secondary_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'residential_address': forms.TextInput(attrs={'class': 'form-control'}),
            'city_or_town': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'occupation': forms.Select(attrs={'class': 'form-control'}),
            'sector': forms.Select(attrs={'class': 'form-control'}),
            'education_level': forms.Select(attrs={'class': 'form-control'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'father_hometown': forms.TextInput(attrs={'class': 'form-control'}),
            'father_living_status': forms.RadioSelect(),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_hometown': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_living_status': forms.RadioSelect(),
            'next_of_kin_name': forms.TextInput(attrs={'class': 'form-control'}),
            'next_of_kin_relationship': forms.Select(attrs={'class': 'form-control'}),
            'next_of_kin_primary_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'next_of_kin_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'next_of_kin_location': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_primary_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'organisations': forms.SelectMultiple(attrs={'class': 'form-select', 'size': "6", 'multiple': 'multiple',
                                                         'aria-label': "size 6 select"}),
            # 'organisations': forms.Select(attrs={'class': 'form-control','list':['organisations']})
        }


class MemberReligiousCVForm(forms.ModelForm):
    class Meta:
        model = MemberReligiousCV
        fields = "__all__"

        widgets = {
            'member': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'baptism_status': forms.RadioSelect(),
            'baptism_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'baptism_location': forms.TextInput(attrs={'class': 'form-control'}),
            'baptised_by': forms.TextInput(attrs={'class': 'form-control'}),

            'holy_communion_status': forms.RadioSelect(),
            'holy_communion_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'holy_communion_location': forms.TextInput(attrs={'class': 'form-control'}),
            'holy_communion_given_by': forms.TextInput(attrs={'class': 'form-control'}),

            'confirmation_status': forms.RadioSelect(),
            'confirmation_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'confirmation_location': forms.TextInput(attrs={'class': 'form-control'}),
            'confirmed_by': forms.TextInput(attrs={'class': 'form-control'}),

        }