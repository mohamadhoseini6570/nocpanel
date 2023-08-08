from django import forms
from .models import Contract, Customer, Agent, Cloud
from ip.models import Ip
from django.forms.models import inlineformset_factory, InlineForeignKeyField
from django.core.exceptions import ValidationError
from django.contrib.admin import widgets
from cloud.ip_check import all_existing_ips, all_binded_ips

def ip_test(value):
    value = int(value)
    if value >= 16 and value<=30:
        return True
    else:
        raise forms.ValidationError('ff') 

def check_not_dup_ip(new_ips_id_list): # check ips aren't duplicate in any other services
    # new_ips_id_list:  ['15', '16', '17']: <class 'list'>: a list of ip_object.id that
    #  must be converted to a list of ip_object to get their ip/mask
    duplicate = False
    new_ips_obj_list = [] 
    # a converted list of object of new_ips_id_list (from id tp object)
    # new_ips_obj_list: [<Ip: 18.18.18.18/32>, <Ip: 19.19.19.19/32>, <Ip: 20.20.20.20/32>]
    # : <class 'list'>
    for any_ip_id in new_ips_id_list: # any_ip_id is a ip_object_id
        any_ip_obj = Ip.objects.get(id=any_ip_id) # any_ip_obj is ip_object
        # any_ip_obj:  18.18.18.18/32
        # typeof_any_ip_obj:  <class 'ip.models.Ip'>
        # any_ip_obj:  19.19.19.19/32
        # typeof_any_ip_obj:  <class 'ip.models.Ip'>
        # any_ip_obj:  20.20.20.20/32
        # typeof_any_ip_obj:  <class 'ip.models.Ip'>
        new_ips_obj_list.append(any_ip_obj) # new_ips_obj_list has ip and subnet_mask fields
       
    for new_ip in new_ips_obj_list:
        # new_ip:  18.18.18.18/32 : <class 'ip.models.Ip'>  
        # new_ip.ip:  18.18.18.18 : <class 'str'>
        
        for binded_ip in all_binded_ips(): # binded_ip is ip without subnet_mask
            # binded_ip:  1.1.1.1 : <class 'str'>
            # all_binded_ips():  ['1.1.1.1', '100.100.100.100', '10.10.10.10', '100.100.100.100', '91.91.91.91', '1.1.1.1', '2.2.2.2', '3.3.3.3',
            # Type_of_all_binded_ips:  <class 'list'>
            if binded_ip == new_ip.ip:
                duplicate = True
            
    if duplicate:
        raise ValidationError("حداقل یکی از IPها تکراری است !")
    else:
        return True

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
        label = 'آی پی ها', validators=[check_not_dup_ip])
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


class CloudForm2(forms.ModelForm):
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
        widget=forms.SelectMultiple(attrs={'class' : 'select', 'data-mdb-filter':'true'}),
        label = 'آی پی ها', validators=[check_not_dup_ip])
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
        label = 'آی پی ها', validators=[check_not_dup_ip])
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

    