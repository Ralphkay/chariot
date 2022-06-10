from django.contrib import admin

# Register your models here.
from cashbook.models import CashBookIncome, CashBookExpenditure, CashBook

admin.site.register(CashBook)
admin.site.register(CashBookIncome)
admin.site.register(CashBookExpenditure)