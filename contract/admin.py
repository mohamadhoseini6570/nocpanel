from django.contrib import admin
from .models import Contract
from .forms import ContractForm2
from django import forms

class ContractAdmin(admin.ModelAdmin):
    form = ContractForm2
    
admin.site.register(Contract, ContractAdmin)