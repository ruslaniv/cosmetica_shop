from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
  """Define a model manager for Custom User model
    This is required since the default "username" field is replaced with "email" field.
  """
  use_in_migrations = True

  def _create_user(self, email, password, **extra_fields):
    """Create a User with the given email and password.
    A base, internal Django method for creating a User instance.
    """
    if not email:
      raise ValueError(_('You must provide email address'))
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password=None, **extra_fields):
    """Create a regular User with the given email and password."""
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, password, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    """Create a SuperUser with the given email and password."""
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    if extra_fields.get('is_staff') is not True:
      raise ValueError(_('Superuser must have "is_staff" set to "True"'))
    if extra_fields.get('is_superuser') is not True:
      raise ValueError(_('Superuser must have "is_superuser" set to "True"'))
    return self._create_user(email, password, **extra_fields)