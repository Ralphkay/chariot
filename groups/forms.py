from django import forms

from groups.models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control', 'id': 'summernote'}),
        }