from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    objective = models.TextField(max_length=255)
    start_date = models.DateField(max_length=255)
    estimated_end_date = models.DateField(max_length=255)
    estimated_cost = models.FloatField(null=False, blank=False, default=0.00)
    estimated_scope = models.TextField(null=False, blank=False)
    project_manager = models.CharField(max_length=255, null=True, blank=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class ProjectMonetaryContribution(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    contributor = models.CharField(max_length=255, null=True, blank=True)
    amount = models.FloatField(null=False, blank=False, default=0.00)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project Monetary Contribution"
        verbose_name_plural = "Project Monetary Contributions"


class ProjectItemContribution(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    item = models.CharField(max_length=255, blank=False, null=False)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    contributor = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=255, blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project Item Contribution"
        verbose_name_plural = "Project Item Contributions"


class ProjectExpense(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    item = models.CharField(max_length=255, blank=False, null=False)
    amount = models.FloatField(null=False, blank=False, default=0.00)
    purpose_of_expense = models.TextField(null=False, blank=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


def document_path_directory(instance, filename):
    return f"uploads/{instance.project}/{filename}"


class ProjectDocument(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    document_name = models.CharField(max_length=255, null=False, blank=False)
    document_upload = models.FileField(upload_to=document_path_directory, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project Note"
        verbose_name_plural = "Project Notes"


class ProjectNote(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    note = models.TextField(null=False, blank=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Project Note"
        verbose_name_plural = "Project Notes"