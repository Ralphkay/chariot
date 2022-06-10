from datetime import datetime
from django.core.exceptions import ValidationError

from django.db import models

# Create your models here.
from membership.models import Member


class Levy(models.Model):
    YEAR_CHOICES = []
    MONTH_CHOICES = []
    for r in range(1980, (datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    t_year_choices = tuple(YEAR_CHOICES)

    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    for m in months:
        MONTH_CHOICES.append((m, m))

    m_months_choices = tuple(MONTH_CHOICES)

    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    year = models.IntegerField(null=False, blank=False, choices=t_year_choices, default=datetime.now().year)
    month = models.CharField(max_length=100, null=False, blank=False, choices=m_months_choices,
                             default=datetime.now().year)
    month_levy_paid = models.FloatField(null=False, blank=False, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Membership Dues'
        verbose_name_plural = 'Membership Dues'
        unique_together = [['year', 'month']]

    def __str__(self):
        return f"Payment – {self.member} – {self.year} - {self.month_levy_paid}"