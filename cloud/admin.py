from django.contrib import admin
from . import models
from django import forms
from .models import Contract, Customer, Agent, Cloud
# from django.core.exceptions import ValidationError
from django.contrib.admin import widgets

class CloudAdmin(admin.ModelAdmin):
    admin.site.register(models.Cloud)
    # form = CloudForm

