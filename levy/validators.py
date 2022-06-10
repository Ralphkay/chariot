from django.core.exceptions import ValidationError


# from django.utils.translation import ugettext as _


def validate_monthly_levy_paid(value):
    print("validating=>", type(value))
    if float(value) == 0:
        raise ValidationError('Levy must be more than Zero')
    return value