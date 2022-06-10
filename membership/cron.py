from membership.models import TryTest


def my_cron_job():
    TryTest.objects.create(name="Just be okay with God's movement")
    return True