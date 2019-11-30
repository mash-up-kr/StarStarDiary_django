from django.db import models
from django.utils import timezone


class TimeStamped(models.Model):
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True
