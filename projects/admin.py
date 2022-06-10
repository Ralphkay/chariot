from django.contrib import admin

# Register your models here.
from projects.models import Project, ProjectMonetaryContribution, ProjectExpense, ProjectDocument, \
    ProjectNote, ProjectItemContribution

admin.site.register(Project)
admin.site.register(ProjectMonetaryContribution)
admin.site.register(ProjectItemContribution)
admin.site.register(ProjectExpense)
admin.site.register(ProjectDocument)
admin.site.register(ProjectNote)