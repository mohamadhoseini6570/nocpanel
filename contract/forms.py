from django import forms
from .models import Contract
from django.forms.models import inlineformset_factory, InlineForeignKeyField
from django.core.exceptions import ValidationError
from django_jalali.forms import jDateTimeField, jDateField
from django_jalali.admin.widgets import AdminSplitjDateTime, AdminjDateWidget

class ContractForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='نام قرارداد') 
    start_time = jDateField(widget=AdminjDateWidget(),
        label='تاریخ شروع')
    end_time = jDateField(widget=AdminjDateWidget(),
        label='تاریخ پایان')
    contract_time = jDateField(widget=AdminjDateWidget(),
        label='تاریخ انعقاد')
    state_choices = (
        ('فعال', 'فعال'),
        ('در حال تمدید', 'در حال تمدید'),
        ('پیش نویس', 'پیش نویس'),
        ('منقضی کمتر از 30 روز', 'منقضی کمتر از 30 روز'),
        ('منقضی', 'منقضی'),
    )
    state = forms.CharField(widget=forms.Select(choices=state_choices,
        attrs={'class': 'form-control'}), label='وضعیت')
    notes = forms.CharField(widget=forms.Textarea(
        attrs={'rows':3, 'class': 'form-control'}), label='توضیحات')

def notes_validator(value: str):
    if 'تست' in value:
        raise ValidationError("کلمه تست غیر مجاز است!")
    else:
        return value

class ContractForm2(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),
        label='نام قرارداد') 
    start_time = jDateField(widget=AdminjDateWidget(),
        label='تاریخ شروع')
    end_time = jDateField(widget=AdminjDateWidget(),
        label='تاریخ پایان')
    contract_time = jDateField(widget=AdminjDateWidget(),
        label='تاریخ انعقاد')
    state_choices = (
        ('فعال', 'فعال'),
        ('در حال تمدید', 'در حال تمدید'),
        ('پیش نویس', 'پیش نویس'),
        ('منقضی کمتر از 30 روز', 'منقضی کمتر از 30 روز'),
        ('منقضی', 'منقضی'),
    )
    state = forms.CharField(widget=forms.Select(choices=state_choices,
        attrs={'class': 'form-control'}), label='وضعیت')
    notes = forms.CharField(widget=forms.Textarea(
        attrs={'rows':3, 'class': 'form-control'}), label='توضیحات', validators=[notes_validator])
    
    class Meta: 
        model = Contract
        fields = '__all__'
    
    def clean(self):
        start_time = self.cleaned_data['start_time']
        end_time = self.cleaned_data['end_time']
        # if start_time and end_time:
        if start_time > end_time: #https://stackoverflow.com/questions/31727564/validating-two-fields-at-the-same-time
            raise ValidationError("تاریخ شروع از تاریخ پایان بزرگتر است!")

        return self.cleaned_data
