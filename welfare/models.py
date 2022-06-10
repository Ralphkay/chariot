import datetime

from django.db import models
from django.db.models import Sum

# Create your models here.

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from membership.models import Member


class Welfare(models.Model):
    welfare_title = models.CharField(max_length=255, blank=False, null=False)
    welfare_description = models.TextField(blank=True, null=True)
    deadline = models.DateField(blank=False, null=False)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.welfare_title}"

    # @property
    # def total_sum_of_contribution(self):
    #     total_sum_contribution = WelfareContribution.objects.filter(welfare=self).aggregate(
    #         Sum('amount_contributed'))
    #
    #     return total_sum_contribution['amount_contributed__sum']

    @property
    def check_welfare_active_status(self):
        if datetime.datetime.today().date() > self.deadline.date():
            return False
        else:
            return True


class WelfareContribution(models.Model):
    """
        General welfare contribution by members towards events such as funerals, sick etc.
    """
    welfare = models.ForeignKey('Welfare', related_name='welfare_contributions', on_delete=models.CASCADE)
    member = models.ForeignKey(Member, related_name='member_welfare_contributions', on_delete=models.CASCADE)

    amount_contributed = models.FloatField(null=False, blank=False, default=0.00)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.welfare} – {self.amount_contributed} – {self.member}"

    def check_deadline(self):
        if datetime.datetime.today().date() > self.welfare.deadline.date():
            return True

    def clean(self):
        if self.check_deadline():
            raise ValidationError({
                'welfare': 'Welfare Deadline expired'
            })

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class WelfareMembershipLevy(models.Model):
    """
    Welfare contribution of members. This in some churches is
    a required contribution.
    """
    YEAR_CHOICES = []
    MONTH_CHOICES = []
    for r in range(1980, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    t_year_choices = tuple(YEAR_CHOICES)

    months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']
    for m in months:
        MONTH_CHOICES.append((m, m))

    m_months_choices = tuple(MONTH_CHOICES)

    member = models.ForeignKey(Member, null=False, blank=False, on_delete=models.CASCADE)
    year = models.IntegerField(null=True, blank=True, choices=t_year_choices, default=datetime.datetime.now().year)
    month = models.CharField(max_length=100, null=True, blank=True, choices=m_months_choices,
                             default=datetime.datetime.now().year)
    month_welfare_paid = models.FloatField(null=True, blank=True, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Welfare Membership Dues'
        verbose_name_plural = 'Welfare Membership Dues'
        unique_together = [['month', 'year']]

    def __str__(self):
        return f"Payment – {self.member} – {self.year} - {self.month_welfare_paid}"