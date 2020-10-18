from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from .manager import CustomUserManager


class CustomUser(AbstractUser):
  username = None
  email = models.EmailField(_('email address'), unique=True)
  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []
  objects = CustomUserManager()

  nick = models.CharField(_('nickname'), max_length=128, unique=True)

  def get_absolute_url(self):
    return reverse('user_detail', kwargs={'pk': self.pk})

  def __str__(self):
    return self.email

