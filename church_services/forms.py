from django import forms

from church_services.models import ChurchService


class ChurchServiceForm(forms.ModelForm):
    class Meta:
        model = ChurchService
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'id': 'summernote'})
        }