from django.contrib import admin

# Register your models here.
from shortner.models import Url, User

admin.site.register(Url)
