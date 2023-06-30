from django.contrib import admin
from . import models

class AgentAdmin(admin.ModelAdmin):
    admin.site.register(models.Agent)
