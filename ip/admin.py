from django.contrib import admin
from . import models
from django import forms

class IpAdmin(admin.ModelAdmin):
    admin.site.register(models.Ip)