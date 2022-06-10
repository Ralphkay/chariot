from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.utils.translation import gettext_lazy as _


# from simple_email_confirmation.models import SimpleEmailConfirmationUserMixin


# class CustomUserManager(BaseUserManager):
#


class User(AbstractUser):
    email = models.EmailField(_('Email'), unique=True)
    username = models.CharField(_('Username'), unique=True, max_length=12)
    first_name = models.CharField(_('First Name'), max_length=255)
    last_name = models.CharField(_('Last Name'), max_length=255)
    is_active = models.BooleanField(_('Is Active'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role', 'username']

    def __str__(self):
        return self.username


class ActivateUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=300, blank=False, null=False)
    expiry = models.DateTimeField(blank=False, null=False)
    is_activated = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.email} - {self.is_activated}"


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = models.ImageField(default='default_profile_photo.jpg', blank=True, null=True,
                                      upload_to='user_profile_photos')
    role = models.CharField(max_length=12, default='Administrator')

    @property
    def get_profile_photo_url(self):
        if self.profile_photo and hasattr(self.profile_photo, 'url'):
            return self.profile_photo.url
        else:
            return "/media/default_profile_photo.jpg"