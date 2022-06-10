from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
from projects.forms import ProjectForm, ProjectMonetaryContributionForm, ProjectItemContributionForm, \
    ProjectExpenseForm, ProjectDocumentForm
from projects.models import Project, ProjectMonetaryContribution, ProjectItemContribution, ProjectExpense, \
    ProjectDocument


def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects,
        'table_name': 'Project Data',
        'dbtn': 'project-download'
    }
    return render(request, 'projects/projects.html', context)


def create_project(request):
    form = ProjectForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Record successfully created')
            return redirect('projects')
        else:
            context = {'form': form}
    return render(request, 'projects/create-project.html', context)


def edit_project(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)
    context = {'form': form, 'project': project}
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, f'Record successfully updated')
            return redirect('projects')
        else:
            context = {'form': form, 'project': project}
    return render(request, 'projects/edit-project.html', context)


def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('projects')
    return None


# PROJECT MONETARY CONTRIBUTION
def project_monetary_contributions(request, project_pk):
    project = Project.objects.get(pk=project_pk)
    project_monetary_contributions = ProjectMonetaryContribution.objects.filter(project=project)
    context = {
        'project': project,
        'project_monetary_contributions': project_monetary_contributions,
        'table_name': 'Project Monetary Contributions Data',
        'dbtn': 'project-monetary-contribution-download'
    }
    return render(request, 'project-monetary-contributions/project-monetary-contributions.html', context)


def create_project_monetary_contribution(request, project_pk):
    project = Project.objects.get(pk=project_pk)
    form = ProjectMonetaryContributionForm(request.POST or None, initial={'project': project})
    context = {'form': form, 'project': project}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Record successfully created')
            return redirect('project-monetary-contributions', project_pk=project.id)
        else:
            context = {'form': form}
    return render(request, 'project-monetary-contributions/create-project-monetary-contribution.html', context)


def edit_project_monetary_contribution(request, project_pk, pmc_pk):
    project = Project.objects.filter(id=project_pk).get()
    pmc = ProjectMonetaryContribution.objects.filter(id=pmc_pk).get()
    form = ProjectMonetaryContributionForm(request.POST or None, instance=pmc)
    context = {'form': form, 'project': project, 'pmc': pmc}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Record successfully created')
            return redirect('project-monetary-contributions', project_pk=project.id)
        else:
            context = {'form': form}
    return render(request, 'project-monetary-contributions/edit-project-monetary-contribution.html', context)


def delete_project_monetary_contribution(request, project_pk, pmc_pk):
    project = Project.objects.filter(id=project_pk).get()
    pmc = ProjectMonetaryContribution.objects.filter(id=pmc_pk).get()
    if request.method == 'POST':
        pmc.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('project-monetary-contributions', project_pk=project.id)
    return None


def project_item_contributions(request, project_pk):
    project = Project.objects.get(pk=project_pk)
    project_item_contributions = ProjectItemContribution.objects.filter(project=project)
    context = {
        'project': project,
        'project_item_contributions': project_item_contributions,
        'table_name': 'Project Item Contributions Data',
        'dbtn': 'project-item-contribution-download'
    }
    return render(request, 'project-inventory/project-item-contributions.html', context)


def create_project_item_contribution(request, project_pk):
    project = Project.objects.get(pk=project_pk)
    form = ProjectItemContributionForm(request.POST or None, initial={'project': project})
    context = {'form': form, 'project': project}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Record successfully created')
            return redirect('project-item-contributions', project_pk=project.id)
        else:
            context = {'form': form}
    return render(request, 'project-inventory/create-project-item-contribution.html', context)


def edit_project_item_contribution(request, project_pk, pmc_pk):
    project = Project.objects.filter(id=project_pk).get()
    pmc = ProjectItemContribution.objects.filter(id=pmc_pk).get()
    form = ProjectItemContributionForm(request.POST or None, instance=pmc)
    context = {'form': form, 'project': project, 'pmc': pmc}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Record successfully created')
            return redirect('project-item-contributions', project_pk=project.id)
        else:
            context = {'form': form}
    return render(request, 'project-inventory/edit-project-item-contribution.html', context)


def delete_project_item_contribution(request, project_pk, pmc_pk):
    project = Project.objects.filter(id=project_pk).get()
    pmc = ProjectItemContribution.objects.filter(id=pmc_pk).get()
    if request.method == 'POST':
        pmc.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('project-item-contributions', project_pk=project.id)
    return None


# project expense functions

def project_expenses(request, project_pk):
    project = Project.objects.get(pk=project_pk)
    project_expenses = ProjectExpense.objects.filter(project=project)
    context = {
        'project': project,
        'project_expenses': project_expenses,
        'table_name': 'Project Expenses Data',
        'dbtn': 'project-expenses-download'
    }
    return render(request, 'project-expenses/project-expenses.html', context)


def create_project_expense(request, project_pk):
    project = Project.objects.get(pk=project_pk)
    form = ProjectExpenseForm(request.POST or None, initial={'project': project})
    context = {'form': form, 'project': project}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Record successfully created')
            return redirect('project-expenses', project_pk=project.id)
        else:
            context = {'form': form}
    return render(request, 'project-expenses/create-project-expense.html', context)


def edit_project_expense(request, project_pk, pmc_pk):
    project = Project.objects.filter(id=project_pk).get()
    pmc = ProjectExpense.objects.filter(id=pmc_pk).get()
    form = ProjectExpenseForm(request.POST or None, instance=pmc)
    context = {'form': form, 'project': project, 'pmc': pmc}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Record successfully created')
            return redirect('project-expenses', project_pk=project.id)
        else:
            context = {'form': form}
    return render(request, 'project-expenses/edit-project-expense.html', context)


def delete_project_expense(request, project_pk, pmc_pk):
    project = Project.objects.filter(id=project_pk).get()
    pmc = ProjectExpense.objects.filter(id=pmc_pk).get()
    if request.method == 'POST':
        pmc.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('project-expenses', project_pk=project.id)
    return None


# project documents
def project_documents(request, project_pk):
    project = Project.objects.get(pk=project_pk)
    project_documents = ProjectDocument.objects.filter(project=project)
    context = {
        'project': project,
        'project_documents': project_documents,
        'table_name': 'Project Documents Data',
        'dbtn': 'project-documents-download'
    }
    return render(request, 'project-documents/project-documents.html', context)


def create_project_document(request, project_pk):
    project = Project.objects.get(pk=project_pk)
    form = ProjectDocumentForm(initial={'project': project})
    context = {'form': form, 'project': project}
    #
    if request.method == 'POST':
        form = ProjectDocumentForm(request.POST, request.FILES, initial={'project': project.id})
        print(request.FILES, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Record successfully created')
            return redirect('project-documents', project_pk=project.id)
        else:
            context = {'form': form, 'project': project}
    return render(request, 'project-documents/create-project-document.html', context)


def edit_project_document(request, project_pk, pmc_pk):
    project = Project.objects.filter(id=project_pk).get()
    pmc = ProjectDocument.objects.filter(id=pmc_pk).get()
    form = ProjectDocumentForm(request.POST or None, request.FILES or None, instance=pmc)
    context = {'form': form, 'project': project, 'pmc': pmc}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f'Record successfully created')
            return redirect('project-documents', project_pk=project.id)
        else:
            context = {'form': form, 'project': project, 'pmc': pmc}
    return render(request, 'project-documents/edit-project-document.html', context)


def delete_project_document(request, project_pk, pmc_pk):
    project = Project.objects.filter(id=project_pk).get()
    pmc = ProjectDocument.objects.filter(id=pmc_pk).get()
    if request.method == 'POST':
        pmc.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('project-documents', project_pk=project.id)
    return None