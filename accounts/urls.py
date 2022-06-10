from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView
from django.urls import path, include, reverse_lazy

from accounts.views import register_user, login_user, logout_user, sent_confirm_view, confirm_email_view

urlpatterns = [

                path('login/', login_user, name='login'),
                path('logout/', logout_user, name='logout'),
                path('register/', register_user, name='register_user'),
                path('confirm-email/<str:token>', confirm_email_view, name='confirm-view'),
                path('go-confirm-email/', sent_confirm_view, name='confirmation-message-view'),


]