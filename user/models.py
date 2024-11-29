from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.models import UuidModel
from user.groups import UserGroup


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def in_group(self, group_name):
        return self.groups.filter(name=group_name).exists()

    @property
    def is_staff(self):
        return self.in_group(UserGroup.ADMIN)

    @property
    def is_superuser(self):
        return self.in_group(UserGroup.ADMIN)

    class Meta:
        abstract = True


class MechaUser(UuidModel, User):
    pass
