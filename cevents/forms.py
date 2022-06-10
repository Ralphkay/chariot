from random import choices

from django import forms

from cevents.models import ChurchEvent


class ChurchEventForm(forms.ModelForm):
    ctypes = (
        ('one-time', 'One-Time'),
        ('recurring', 'Recurring'),
    )
    # types = forms.ChoiceField(choices=ctypes, widget=forms.RadioSelect),

    class Meta:
        model = ChurchEvent
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control','id':'summernote', 'rows': 5}),
            'start_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'end_date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'type': forms.RadioSelect(attrs={'class': ''}),
            'email_recipients': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }