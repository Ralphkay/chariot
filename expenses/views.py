from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from expenses.forms import ExpenseForm
from expenses.models import Expense
from django.core.paginator import Paginator

from membership.models import Member


def expenses(request):
    all_expenses = Expense.objects.all()
    context = {
        'expenses': all_expenses,
        'table_name': 'Church Expenses Data',
        'dbtn': 'expenses-download'
    }
    return render(request, 'expenses/expenses.html', context)


def number_of_members_in_organisation(org):
    number_of_members = Member.objects.filter(organisations__exact=org).count()
    return number_of_members


def edit_expense(request, pk):
    expense = Expense.objects.get(id=pk)
    form = ExpenseForm(instance=expense)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, f"Record updated successfully")
            return redirect('expenses')

    context = {
        'form': form,
        'expense': expense,
    }

    return render(request, 'expenses/edit_expense_form.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(id=pk)
    if request.method == 'POST':
        expense.delete()
        messages.success(request, f"Record deleted successfully")
        return redirect('expenses')
    return None


def create_expense(request):
    form = ExpenseForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, f"Record saved successfully")
            return redirect('expenses')
    context = {
        'form': form
    }
    return render(request, 'expenses/create_expense_form.html', context)