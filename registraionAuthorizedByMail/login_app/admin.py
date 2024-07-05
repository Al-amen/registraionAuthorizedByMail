from django.contrib import admin

# Register your models here.
from login_app import models

admin.site.register(models.Profile)