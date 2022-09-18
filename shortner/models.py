import datetime

from django.db import models


# Create your models here.
from accounts.models import User


class Url(models.Model):
    short_id = models.CharField(max_length=10, primary_key=True, blank=True)
    link = models.CharField(max_length=2048)
    created_at = models.DateField(default=datetime.date.today)
    expires_at = models.DateField(default=datetime.date.today)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
