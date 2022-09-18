from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    email_id = models.EmailField(max_length=128, blank=True)
    has_premium = models.BooleanField(default=False)
    url_count = models.PositiveIntegerField(default=0)

