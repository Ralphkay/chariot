from django import forms

from projects.models import Project, ProjectMonetaryContribution, ProjectItemContribution, ProjectExpense, \
    ProjectDocument


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'objective': forms.Textarea(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estimated_end_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'estimated_cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'estimated_scope': forms.Textarea(attrs={'class': 'form-control', 'id': 'summernote'}),
            'project_manager': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ProjectMonetaryContributionForm(forms.ModelForm):
    class Meta:
        model = ProjectMonetaryContribution
        fields = "__all__"

        widgets = {
            'project': forms.HiddenInput(),
            'contributor': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ProjectItemContributionForm(forms.ModelForm):
    class Meta:
        model = ProjectItemContribution
        fields = "__all__"

        widgets = {
            'project': forms.HiddenInput(),
            'contributor': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class ProjectExpenseForm(forms.ModelForm):
    class Meta:
        model = ProjectExpense
        fields = "__all__"

        widgets = {
            'project': forms.HiddenInput(),
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'purpose_of_expense': forms.Textarea(attrs={'class': 'form-control'}),
            'contributor': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class ProjectDocumentForm(forms.ModelForm):
    class Meta:
        model = ProjectDocument
        fields = "__all__"

        widgets = {
            'project': forms.HiddenInput(),
            'document_name': forms.TextInput(attrs={'class': 'form-control'}),
            'document_upload': forms.FileInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'id': 'summernote'}),
        }