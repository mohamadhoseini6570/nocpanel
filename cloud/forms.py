from django import forms
from .models import Contract
from django.forms.models import inlineformset_factory, InlineForeignKeyField
from django.core.exceptions import ValidationError
