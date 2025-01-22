from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    ROLE_TYPES = [
        ('HIRING', _('HIRING')),
        ('WORKER', _('WORKER')),
    ]

    username = None
    email = models.EmailField(_("email address"), unique=True)
    custom_role = models.CharField(_("custom role"), max_length=20, choices=ROLE_TYPES, default='HIRING')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    SERVICE_CHOICES = [
        ('HOME CARE', 'HOME CARE'),
        ('CHILD CARE', 'CHILD CARE'),
        ('ELDER CARE', 'ELDER CARE'),
        ('PET CARE', 'PET CARE'),
    ]
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    services = models.JSONField(default=list, blank=True)

    def __str__(self):
        return self.user.email
