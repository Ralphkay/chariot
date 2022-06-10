from django.urls import path
from cashbook.views import setup_cashbook, generate_total_contributions

urlpatterns = [
    path('setup/', setup_cashbook, name='setup-cashbook'),
    path('gtc/', generate_total_contributions, name='generate-total-contributions'),
]