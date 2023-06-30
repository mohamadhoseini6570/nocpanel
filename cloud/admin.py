from django.contrib import admin
from . import models

class CloudAdmin(admin.ModelAdmin):
    admin.site.register(models.Cloud)
