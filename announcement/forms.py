from django import forms

from announcement.models import Announcement


class AnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': '', 'rows': '5', 'id': 'summernote'}),
        }