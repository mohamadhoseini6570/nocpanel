from django.contrib import admin
from . import models

class ContractAdmin(admin.ModelAdmin):
    admin.site.register(models.Contract)