from cryptography.fernet import Fernet

from accounts.models import ActivateUser
from churchclicks import settings
from datetime import datetime, timedelta

# Using current time
ini_time_for_now = datetime.now()

future_date_after_7days = ini_time_for_now + \
                          timedelta(days=settings.EMAIL_CONFIRMATION_PERIOD_DAYS)


def generate_confirmation_token(user):
    key = b'-6Cgt41UQ0zkUavQMIPz8ZeUP2DsnyW5KTvtwrihUy0='

    f = Fernet(key)
    user_email = user.email
    expiry = future_date_after_7days
    t = f"{user_email}/{expiry}"
    b = bytes(t, encoding='utf-8')
    token = f.encrypt(b)
    decode_token = token.decode('utf-8')
    ActivateUser.objects.create(user=user, token=decode_token, expiry=expiry)
    return decode_token


def decode_token(token):
    b = bytes(token, encoding='utf-8')
    key = b'-6Cgt41UQ0zkUavQMIPz8ZeUP2DsnyW5KTvtwrihUy0='
    f = Fernet(key)
    text = f.decrypt(b)
    text = text.decode('utf-8')
    return text