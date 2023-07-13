from django import forms
from .models import Customer
from django.forms.models import inlineformset_factory, InlineForeignKeyField
from django.core.exceptions import ValidationError

class CustomerForm(forms.ModelForm):
    commercialname = forms.CharField(widget=forms.TextInput(attrs=
        {'class': 'form-control'}), label='نام تجاری') 
    brand = forms.CharField(widget=forms.TextInput(attrs=
        {'class': 'form-control'}), label='برند')
    kindchoices = (
        ('عادی', 'عادی'),
        ('ویژه', 'ویژه'),
    )
    kind = forms.CharField(widget=forms.Select(choices=kindchoices,
        attrs={'class': 'form-control'}), label='نوع')
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='شهر')
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='آدرس')
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='تلفن')
    notes = forms.CharField(widget=forms.Textarea(
        attrs={'rows':3, 'class': 'form-control'}), label='توضیحات')
    
    class Meta: 
        model = Customer
        fields = '__all__'

