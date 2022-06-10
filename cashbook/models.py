from email.policy import default

from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

# Create your models here.
from expenses.models import Expense
from offerings.models import Offering


class CashBook(models.Model):
    book_name = models.CharField(max_length=255, null=False, blank=False)
    funds_currently_at_hand = models.FloatField(null=False, blank=False, default=0.00)
    current_expenditure = models.FloatField(null=False, blank=False, default=0.00)

    def __str__(self):
        return self.book_name


class CashBookIncome(models.Model):
    amount = models.FloatField(null=False, blank=False, default=0.00)
    income_type = models.CharField(max_length=255, null=False, blank=False)
    income_instance = models.CharField(max_length=255, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return f"{self.income_type} - {self.amount}"


class CashBookExpenditure(models.Model):
    amount = models.FloatField(null=False, blank=False, default=0.00)
    expense_type = models.CharField(max_length=255, null=False, blank=False)
    expense_instance = models.CharField(max_length=255, null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=False)

    def __str__(self):
        return f"{self.expense_type} - {self.amount}"


# signals for expenditure
@receiver(post_save, sender=Expense)
def create_ledger_expense_record(sender, instance, created, **kwargs):
    if created:
        expenditure = CashBookExpenditure(
            amount=instance.amount,
            expense_type=sender.__class__,
            expense_instance=instance
        )
        expenditure.save()


@receiver(pre_save, sender=Expense)
def update_ledger_expense_record(sender, instance, update_fields, **kwargs):
    if instance.id is not None:
        expenditure = CashBookExpenditure.objects.filter(expense_instance=instance).get()
        if expenditure is not None:
            expenditure.amount = instance.amount
            expenditure.save()
        else:
            pass


# signals for income
@receiver(post_save, sender=Offering)
def create_ledger_income_record(sender, instance, created, **kwargs):
    if created:
        income = CashBookIncome(
            amount=instance.amount,
            income_type=sender.__class__,
            income_instance=instance
        )
        income.save()


@receiver(pre_save, sender=Offering)
def update_ledger_income_record(sender, instance, update_fields, **kwargs):
    if instance.id is not None:
        income = CashBookIncome.objects.filter(income_instance=instance).get()
        print('done', income)
        if income is not None:
            income.amount = instance.amount
            income.save()
        else:
            pass