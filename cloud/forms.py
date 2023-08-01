from django import forms
from .models import Contract, Customer, Agent, Cloud
from ip.models import Ip
from django.forms.models import inlineformset_factory, InlineForeignKeyField
from django.core.exceptions import ValidationError
from django.contrib.admin import widgets

def ip_test(value):
    value = int(value)
    if value >= 16 and value<=30:
        return True
    else:
        raise forms.ValidationError('ff') 

class CloudForm(forms.ModelForm):
    class Meta:
        model = Cloud
        fields = '__all__'
    
    sizechoices = (
        ('Micro', 'Micro'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('XLarge', 'XLarge'),
        ('XXLarge', 'XXLarge'),
    )
    size = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices= sizechoices,
        label='سایز', error_messages={'required':'پرش کن!'},
        required=True, help_text='سایز سرویس را وارد کنید')
    ips = forms.ModelMultipleChoiceField(queryset=Ip.objects.all(),
        widget=forms.SelectMultiple(attrs={'class' : 'filter-multi-select', 'id':'ips'}),
        label = 'آی پی ها')
    contract = forms.ModelChoiceField(queryset=Contract.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'contract'}), label = 'قرارداد')
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'customer'}), label = 'مشترک')
    agents = forms.ModelMultipleChoiceField(queryset=Agent.objects.all(),
        widget=forms.SelectMultiple(attrs={'class' : 'filter-multi-select', 'id':'agents'}),
        label = 'نماینده') # <SELECT><OPTION> https://github.com/andreww1011/filter-multi-select
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'class': 'form-control'})
        ,label='توضیحات', validators=[ip_test]) 
    error_css_class = 'error'
    required_css_class = 'bold'

class CloudForm1(forms.Form):
    sizechoices = (
        ('Micro', 'Micro'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('XLarge', 'XLarge'),
        ('XXLarge', 'XXLarge'),
    )
    size = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}),choices= sizechoices,
        label='سایز', error_messages={'required':'پرش کن!'},
        required=True, help_text='سایز سرویس را وارد کنید')
    # ip = forms.GenericIPAddressField(widget=forms.TextInput(attrs= {'class': 'form-control'}),
    #     label='ip', error_messages={'required':'پرش کن!'},
    #     required=True, help_text='آدرس آی پی سرویس را وارد کنید')
    ips = forms.ModelMultipleChoiceField(queryset=Ip.objects.all(),
        widget=forms.SelectMultiple(attrs={'class' : 'filter-multi-select', 'id':'ips'}),
        label = 'آی پی ها')
    subnet_mask = forms.CharField(widget=forms.TextInput(attrs= {'class': 'form-control'}),
        label='subnet mask', error_messages={'required':'پرش کن!'},
        required=True, help_text='آدرس آی پی سرویس را وارد کنید')
    contract = forms.ModelChoiceField(queryset=Contract.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'contract'}), label = 'قرارداد')
    customer = forms.ModelChoiceField(queryset=Customer.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control', 'id': 'customer'}), label = 'مشترک')
    agents = forms.ModelMultipleChoiceField(queryset=Agent.objects.all(),
        widget=forms.SelectMultiple(attrs={'class' : 'filter-multi-select', 'id':'agents'}),
        label = 'نماینده') # <SELECT><OPTION> https://github.com/andreww1011/filter-multi-select
    notes = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'class': 'form-control'})
        ,label='توضیحات', validators=[ip_test]) 
    error_css_class = 'error'
    required_css_class = 'bold'

    