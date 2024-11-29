from django.db import models

from core.models import UuidModel


class ModelConfig(UuidModel):
    value = models.TextField()
